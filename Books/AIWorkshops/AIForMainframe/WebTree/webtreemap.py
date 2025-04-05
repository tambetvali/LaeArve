# # File Tree Mapper Documentation
# 
# This Python file implements a mapper that connects your local hard‑drive file tree (the “source”)
# with its web‑mapped view (the “target”). The local source tree (the physical code tree) is scanned 
# and every file or folder is stored as a node in an AnyTree hierarchy. Each node gets a computed 
# web URL. The mapping uses three folder “parameters”:
#
# - **source_root**: The physical file tree root.
# - **target_folder**: A folder inside the source that becomes the site’s “main” content. Files/folders 
#   inside this folder are mapped directly under the base web address.
# - **reflection_folder**: All files/folders that are not inside target_folder are “reflected” and 
#   mapped under this folder inside the web URL.
#
# For example, if:
#   • source_root = "/code_root"
#   • target_folder = "site"
#   • reflection_folder = "reflector"
#   • webaddress = "http://example.com"
#
# Then a physical file at:
#   /code_root/site/sub/page.md
# is mapped to:
#   http://example.com/sub/page.md
#
# Whereas a file at:
#   /code_root/otherdir/readme.md
# is mapped to:
#   http://example.com/reflector/otherdir/readme.md
#
# The mapper also uses MongoDB to cache file information (hashes, timestamps, and even parsed Markdown 
# “chapter trees”). Markdown files are scanned for headings (using '#' markers) and for special blocks:
#
# • A block with "__name:__ <filenamemapping>" under a chapter title indicates that the chapter is 
#   mapped to a specific file name.
#
# • A block beginning with "@ __self:__ <link target>" is used to mark a self‑target.
#
# • Lines starting with "@@" along with a directive like "__<name>:__ <link>" will have the block removed 
#   and register an accessor (this sample code only marks the occurrence, leaving further processing as future work).
#
# The system supports hooks (pre‑scan and post‑scan) so you can customize behavior at key steps.
#
# Finally, two conversion functions are provided:
#   • `physical_to_web()` to convert a hard‑drive (source) path to a web URL;
#   • `web_to_physical()` to convert back.
#
# The testing code at the bottom of the file creates a temporary file layout, builds the file tree (using AnyTree),
# prints it, performs a sample conversion, and then cleans up.

import os
import hashlib
import pymongo
import datetime
import re
import tempfile
import shutil

from anytree import NodeMixin, RenderTree, PreOrderIter

# --- Conversion Functions: Physical Path <-> Web URL ---

def physical_to_web(physical_path, source_root, target_folder, webaddress, reflection_folder):
    """
    Convert a physical file path into a web URL.
    
    The function computes the relative path (from source_root).
    
    - If the first item in the relative path equals target_folder, then that prefix is dropped and
      the remainder is appended directly to the webaddress.
    - Otherwise, the entire relative path is appended to the webaddress under the reflection_folder.
    """
    relative = os.path.relpath(physical_path, source_root)
    # Normalize to URL-style (using forward slashes)
    relative_url = relative.replace(os.sep, "/")
    parts = relative_url.split("/")
    if parts[0] == target_folder:
        # Inside target_folder: remove the target_folder prefix.
        subpath = "/".join(parts[1:])  # may be empty
        if subpath:
            result = webaddress.rstrip("/") + "/" + subpath.lstrip("/")
        else:
            result = webaddress.rstrip("/")
    else:
        # Not inside target_folder: use reflection mapping.
        result = webaddress.rstrip("/") + "/" + reflection_folder.rstrip("/") + "/" + relative_url
    return result

def web_to_physical(web_url, source_root, target_folder, webaddress, reflection_folder):
    """
    Convert a web URL back into the physical file path.
    
    The function removes the webaddress prefix and then tests whether the resulting path begins with
    the reflection_folder name. If so, the remainder is considered relative to source_root.
    Otherwise, the URL is assumed to originate from inside target_folder.
    """
    if not web_url.startswith(webaddress):
        return None
    partial = web_url[len(webaddress):].lstrip("/")
    if partial.startswith(reflection_folder):
        subpath = partial[len(reflection_folder):].lstrip("/")
        return os.path.join(source_root, subpath)
    else:
        return os.path.join(source_root, target_folder, partial)

# --- File Node Class for AnyTree ---
    
class FileNode(NodeMixin):
    """
    FileNode represents a file or folder from the source tree.
    
    Attributes:
      name        : Name of the file or folder.
      source_path : Full physical path on disk.
      parent      : Parent FileNode.
      file_type   : Type of node: "folder", "file", or "markdown".
      web_url     : Mapped web URL (computed via conversion functions).
      hash_value  : MD5 hash of file contents (if a file); None for folders.
      timestamp   : Last modification time (epoch value).
      chapters    : For markdown files, a chapter list (parsed via parse_markdown).
    """
    def __init__(self, name, source_path, parent=None, file_type="folder", web_url=None,
                 hash_value=None, timestamp=None, chapters=None):
        self.name = name
        self.source_path = source_path
        self.parent = parent
        self.file_type = file_type
        self.web_url = web_url
        self.hash_value = hash_value
        self.timestamp = timestamp
        self.chapters = chapters if chapters is not None else []
    
    def __repr__(self):
        return f"FileNode({self.name}, type={self.file_type})"

# --- Markdown Parsing Implementation ---
    
def parse_markdown(file_path):
    """
    Parse a markdown file to extract a rudimentary chapter tree and directives.
    
    This simple parser scans the markdown file for headings (lines starting with "#") and
    searches for special tokens:
      • "__name:__ <filenamemapping>"
      • "@ __self:__ <link target>"
      • Blocks starting with "@@" (and a directive __<name>:__)
    
    Returns:
      A list of chapters, each represented as a dict with:
         - level: the heading level (number of '#' characters)
         - title: the heading text
         - directives: any directives found (a dict)
    """
    chapters = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    level = len(re.match(r"#+", line).group(0))
                    title = line[level:].strip()
                    directives = {}
                    m_name = re.search(r"__name:__\s*(\S+)", title)
                    if m_name:
                        directives["name"] = m_name.group(1)
                    m_self = re.search(r"@ __self:__\s*(\S+)", title)
                    if m_self:
                        directives["self"] = m_self.group(1)
                    # Further patterns (like @@ directives) may be added here.
                    chapters.append({"level": level, "title": title, "directives": directives})
        return chapters
    except Exception as e:
        print(f"Error parsing markdown file {file_path}: {e}")
        return []

# --- File Hash Calculation ---

def compute_file_hash(file_path, block_size=65536):
    """
    Compute an MD5 hash of a file in blocks.
    """
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            buf = f.read(block_size)
            while buf:
                hasher.update(buf)
                buf = f.read(block_size)
        return hasher.hexdigest()
    except Exception as e:
        return None

# --- MongoDB Cache Integration ---
    
class MongoCache:
    """
    MongoCache uses PyMongo to cache file and folder metadata.
    
    Each document in the "filemaps" collection stores a node’s source path, web URL, file hash,
    timestamp, type, and (if applicable) the parsed chapter tree.
    """
    def __init__(self, uri="mongodb://localhost:27017", db_name="filemapper_db"):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["filemaps"]

    def update_node(self, node):
        doc = {
            "source_path": node.source_path,
            "web_url": node.web_url,
            "hash_value": node.hash_value,
            "timestamp": node.timestamp,
            "file_type": node.file_type,
            "chapters": node.chapters,
        }
        # Use source_path as unique identifier.
        self.collection.update_one({"source_path": node.source_path}, {"$set": doc}, upsert=True)

    def get_node(self, source_path):
        return self.collection.find_one({"source_path": source_path})

# --- FileTreeMapper Class ---
    
class FileTreeMapper:
    """
    FileTreeMapper scans a physical source tree, builds an in-memory tree with AnyTree,
    computes the mapped web URLs from physical paths, caches the information in MongoDB,
    and parses Markdown files to gather chapter information.
    
    It also provides a hook interface for adding pre‐ and post‑scan functions.
    """
    def __init__(self, source_root, target_folder, webaddress, reflection_folder):
        self.source_root = source_root
        self.target_folder = target_folder
        self.webaddress = webaddress
        self.reflection_folder = reflection_folder
        self.mongo_cache = MongoCache()
        self.root_node = None
        # Hook lists.
        self.pre_scan_hooks = []
        self.post_scan_hooks = []
    
    def register_pre_scan_hook(self, hook_func):
        self.pre_scan_hooks.append(hook_func)

    def register_post_scan_hook(self, hook_func):
        self.post_scan_hooks.append(hook_func)

    def build_tree(self):
        """
        Traverse the source_root directory and build a tree of FileNode objects.
        Hidden files/directories and __pycache__ are skipped.
        """
        # Call pre-scan hooks.
        for hook in self.pre_scan_hooks:
            hook(self)
        
        # Create the root node.
        self.root_node = FileNode(os.path.basename(self.source_root.rstrip(os.sep)), self.source_root)
        
        # Walk the directory.
        for dirpath, dirnames, filenames in os.walk(self.source_root):
            # --- Filter out hidden directories and __pycache__ directories ---
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
            # --- Filter out hidden files and __pycache__ files (if applicable) ---
            filenames = [f for f in filenames if not f.startswith('.') and f != '__pycache__']
            
            parent_node = self._find_node_by_source_path(self.root_node, dirpath)
            if parent_node is None:
                continue
            
            # Process subdirectories.
            for d in dirnames:
                full_path = os.path.join(dirpath, d)
                web_url = physical_to_web(full_path, self.source_root, self.target_folder,
                                            self.webaddress, self.reflection_folder)
                node = FileNode(d, full_path, parent=parent_node, file_type="folder", web_url=web_url)
                try:
                    node.timestamp = os.path.getmtime(full_path)
                except Exception:
                    node.timestamp = None
                self.mongo_cache.update_node(node)
            
            # Process files.
            for f in filenames:
                full_path = os.path.join(dirpath, f)
                web_url = physical_to_web(full_path, self.source_root, self.target_folder,
                                            self.webaddress, self.reflection_folder)
                file_type = "file"
                chapters = []
                if f.lower().endswith(".md"):
                    file_type = "markdown"
                    chapters = parse_markdown(full_path)
                node = FileNode(f, full_path, parent=parent_node, file_type=file_type, web_url=web_url,
                                chapters=chapters)
                if os.path.isfile(full_path):
                    node.hash_value = compute_file_hash(full_path)
                    try:
                        node.timestamp = os.path.getmtime(full_path)
                    except Exception:
                        node.timestamp = None
                self.mongo_cache.update_node(node)
        
        # Call post-scan hooks.
        for hook in self.post_scan_hooks:
            hook(self)

    def _find_node_by_source_path(self, root, source_path):
        """
        Finds a node in the tree with a matching source_path (normalized).
        """
        for node in PreOrderIter(root):
            if os.path.normpath(node.source_path) == os.path.normpath(source_path):
                return node
        return None
    
    def print_tree(self):
        """
        Print the file tree with each node’s name and mapped web URL using AnyTree’s render utility.
        """
        for pre, fill, node in RenderTree(self.root_node):
            print(f"{pre}{node.name} - {node.web_url}")
    
    def get_node_by_web_url(self, web_url):
        """
        Retrieve a node by its web URL.
        """
        for node in PreOrderIter(self.root_node):
            if node.web_url == web_url:
                return node
        return None

# --- Testing the FileTreeMapper ---

# # File Tree Mapper Testing
#
# In this test, we create a temporary directory structure that simulates a source tree.
# The following structure is created:
#
#   code_root/
#     site/                <-- designated target_folder; mapped directly under webaddress.
#       index.md         (contains a "__name:__" directive)
#     otherfolder/         <-- not inside target_folder; mapped under the reflection_folder.
#       readme.md        (contains an "@ __self:__" directive)
#       script.py        (a simple file)
#
# After creating the structure, we initialize the FileTreeMapper using:
#
#   • source_root = code_root (inside a temporary directory)
#   • target_folder = "site"
#   • reflection_folder = "reflector"
#   • webaddress = "http://example.com"
#
# The mapper scans the file tree, builds the AnyTree, caches node info in MongoDB, prints the tree,
# and then demonstrates a sample conversion from a physical file path to a web URL and back.

if __name__ == "__main__":    
    # Create a temporary directory to simulate the file tree.
    temp_dir = tempfile.mkdtemp(prefix="filetree_")
    print("Temporary directory created:", temp_dir)
    
    # Define parameters.
    source_root = os.path.join(temp_dir, "/home/tvali/LaeArve")
    target_folder = "Books"         # The folder inside the source tree that maps directly.
    reflection_folder = "Books/Reflector"  # The folder used for items not in target_folder.
    webaddress = "http://127.0.0.1:5000"  # Base web URL.
    
    # Create directories.
    os.makedirs(os.path.join(source_root, target_folder), exist_ok=True)
    os.makedirs(os.path.join(source_root, "otherfolder"), exist_ok=True)
    
    # Create a Markdown file inside the target folder.
    index_md_path = os.path.join(source_root, target_folder, "index.md")
    with open(index_md_path, "w", encoding="utf-8") as f:
        f.write("# Home\n__name:__ homepage\nContent of home page.\n")
    
    # Create a Markdown file in another folder.
    readme_md_path = os.path.join(source_root, "otherfolder", "readme.md")
    with open(readme_md_path, "w", encoding="utf-8") as f:
        f.write("# About\n@ __self:__ /about\nMore about content.\n")
    
    # Create a regular file.
    script_py_path = os.path.join(source_root, "otherfolder", "script.py")
    with open(script_py_path, "w", encoding="utf-8") as f:
        f.write("print('Hello world')\n")
    
    # Initialize the mapper.
    mapper = FileTreeMapper(source_root, target_folder, webaddress, reflection_folder)
    
    # Register a pre-scan hook.
    def pre_scan(mapper_instance):
        print("Pre-scan hook triggered.")
    mapper.register_pre_scan_hook(pre_scan)
    
    # Register a post-scan hook.
    def post_scan(mapper_instance):
        print("Post-scan hook triggered.")
    mapper.register_post_scan_hook(post_scan)
    
    # Build the file tree.
    mapper.build_tree()
    
    # Print out the constructed file tree.
    print("\nConstructed File Tree:")
    mapper.print_tree()
    
    # Test conversion: physical to web and back.
    sample_physical = os.path.join(source_root, "otherfolder", "readme.md")
    converted_web = physical_to_web(sample_physical, source_root, target_folder, webaddress, reflection_folder)
    reverted_physical = web_to_physical(converted_web, source_root, target_folder, webaddress, reflection_folder)
    print("\nSample Conversion:")
    print("Physical Path:         ", sample_physical)
    print("Converted Web URL:     ", converted_web)
    print("Reverted Physical Path:", reverted_physical)
    
    # Clean up the temporary directory.
    shutil.rmtree(temp_dir)
    print("\nTemporary directory removed.")
