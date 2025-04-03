# = First Part
# __Code.Position__: StandardImplementation
# Reading the Raw Directories

# These classes are used to navigate directories for various purposes.

# _Notice_:
# This class will be modified to reflect any change in standards about how the file
# tree is reflected, and will remain a standard implementation where one could use
# optimized version. We want to always provide the "open source" functionality of
# having somewhere to start their own projects.

# Notice: we won't break the filenames and folder names, thus we won't check about
# their formats.

# == Imports
#
# Import "os" and "pathlib" for filesystem and file name access.

import os
import pathlib

# Import anytree to provide structured view.

from anytree import Node, RenderTree

# == Class RawDirectory

# Build filesystem access on raw level

# Input: the root folder to process; notice TODO: it's currently relative to my filesystem
root = "/home/tvali/LaeArve"

# This folds files with different extensions into the same node with directory
# with the same name.
class RawNodeDirectory:
    def __init__(self, filename, extension, type, parent):
        self.filename = filename
        self.types = {}
        self.addChild(filename, extension, type, parent)
    
    def addChild(self, filename, extension, type, parent):
        if extension not in self.types:
            self.types[extension] = {}
        self.types[extension]["filename"] = filename
        self.types[extension]["type"] = type # type is "file" or "folder"
        self.types[extension]["parent"] = parent # type is "file" or "folder"
        return self

    # Empty folders are included
    def hasChildren(self):
        for extension in self.types:
            if self.types[extension]["type"] == "folder":
                return True
        return False
    
    # Empty folders are included
    def getChildren(self):
        for extension in self.types:
            if self.types[extension].type == "folder":
                # TODO: it should reuse RawDirectory objects
                return RawDirectory(self.types[extension].parent.dir + "/" +
                                    self.types[extension].filename)
        return None

# The class RawDirectory is a lazy loader of directory nodes from filesystem tree.

# Let's call low-lever Folders Directories, where dir reminds of direction.
class RawDirectory:
    def __init__(self, dir, parent = None, root = None):
        print("Raw reading: ", dir)
        self.dir = dir
        self.root = root
        self.node = self.sepExt(dir)
        self.parent = parent
        self.contain = False
        if parent == None:
            self.root = self
    
    def __str__(self):
        return self.dir

    # Have extension and root name from filename
    def sepExt(self, filename, nodes = None):
        filepath = os.path.join(self.dir, filename)
        if os.path.isfile(filepath):  # Check if it's a file
            # TODO: rather use pathlib to extract extensions?
            base_type = "file"
            base_name = pathlib.Path(filename).stem
            extension = pathlib.Path(filename).suffix
        elif os.path.isdir(filepath):
            base_type = "folder"
            base_name = filename
            extension = ""
        
        if nodes == None:
            return RawNodeDirectory(base_name, extension, base_type, self)
        else:
            return nodes.addChild(base_name, extension, base_type, self)

    def lazyContain(self):
        if self.contain:
            return
        self.contain = True

        self._nodes = {}
        self._types = {}
        self._fold = {}
        for filename in os.listdir(self.dir):
            # TODO: proper ignore list
            if filename[0] == ".": continue # ".git"
            if filename[0] == "_" and filename[1] == "_": continue # "__pycache__"

            node = self.sepExt(filename)
        
            if not node.filename in self._nodes:
                self._nodes[node.filename] = {}
            self._nodes[node.filename] = node

    def nodes(self):
        self.lazyContain() # Lazy loader
        for filename in self._nodes:
            yield filename

    def children(self):
        self.lazyContain() # Lazy load
        for filename in self._nodes:
            if self._nodes[filename].hasChildren():
                yield self._nodes[filename]

#
# --------------------------------------------------------------------------------
# == Second Part:
# Raw Directories => Folder Structure
#

#
# === Helper Class:
# Find the tree.md items and reproject the filesystem
#

# Input is RawDirectory; notice that this smashes any kind of lazy loading of file names,
# because in this implementation we won't optimize: we should get the whole system
# without premature optimizations, where we are _not_ mature.
class ReProjectorHelper:
    def __init__(self, dir):
        self.findTreeNodes(dir)
        self.treePosition = "CommonBranch"

    def checkTreeNode(self, dir):
        # REVIEW: Currently we are case-sensitive here, file name is "tree.md".
        if dir.base_name == "tree" and dir.extension == ".md":
            # Check the first line of tree.md:
            # "__TreePosition__: IdealRoot": variable TreePosition will be set to "IdealRoot"
            # "__TreePosition__: PracticalRoot": variable TreePosition will be set to "PracticalRoot"
            with open('filename.txt', 'r') as file:
                line = file.readline()
                variable, value = line.split(":")
                if variable == "__TreePosition__":
                    treePosition = value
        # We won't delete from dir, we only cache what we already have
        dir.treePosition = treePosition
        if treePosition == "IdealRoot":
            dir.root.idealRoot = self
        elif treePosition == "PracticalRoot":
            dir.root.practicalRoot = self
        return treePosition

    def findTreeNodes(self, dir):
        self.checkTreeNode(dir)
        for node in dir:
            self.findTreeNodes(dir)

#
# === Base Class:
# Create the low-level folder view as served
#

# __Find the tree.md instances in root filesystem of the project, to project it
# into the Moebius shape: inside-out.__ Client becomes priority and programmer
# or manager is less prioritized from outside view, where Books are the
# primary folder and Source Code is quite secondary. Still, while project
# tree must be visible for Open Source, and more or less human/AI-readable.
# We might teach AI to answer with creative Q&A pairs, given such comment
# and the code, thus it could be "Wiki-connected" to have Open Wiki where
# each can add their corrections, version number and / or cache of the version
# of original page; through which they refer to original version in Git, which
# should be a root folder of Spider's reflection: it's a good Spider, which knows
# it's own sites, but relatively exensible to espacially Markdown servings, but
# also HTML for example you can convert it to Markdown, and keep the tags and
# additional references, like XML. I think you can configure some converters
# or especially, AI can show where to add hooks into open source conversion
# libraries, where you need to support their Licence terms and agree to something
# where CC, GPL and probably MIT should be all compatible with my original idea, as
# scientist or programmer or usomething like university user or "hacker" as GPL
# community calls themselves not "literally" might need them for their needs.
reProjectorInstance = ReProjectorHelper(root)

# This would collect all the important elements
# TODO: I think we need to have backlinks collected back into database,
#       like ".laemdb/backlinks/ file under current folder."
# RawNodeFolder can also contain chapter or other parts of the document,
# so in addition to "folders" and "files", it can be "chapters" and "blocks".
class RawNodeFolder:
    def __init__(self, name):
        self.name = name
        self.types = {}
        self.treemd = None
        self.node = Node(self)

    def setParent(self, other):
        self.node.parent = other.node

    # Tree special attribute: None, "Ideal", "Practical"
    def setTreeAttribute(self, treespecial):
        self.treemd = treespecial

    # Add RawDirectoryFolder
    def addFiles(self, rdir):
        for type in rdir.types:
            if type not in self.types: self.types[type] = []
            # We will have different types of things we fold, such as chapters
            # and blocks: we use dictionary for this purpose.
            file = {
                "filename": rdir.types[type].filename,
                "extension": rdir.types[type].filename,
                "type": rdir.types[type].filename
            }
            # We have more than one element of the same type, so we use list append
            self.types[type].append(file)

    def __str__(self):
        return self.name

# Now I call it folder: it's already in abstract level for the user.
class RawFolder:
    def __init__(self, dir):
        self.dir = dir
        self.contain = False
        rdir = RawDirectory(dir)

    def buildDir(self, dir):
        rdir = RawDirectory(dir)
        for filename in rdir.nodes():
            self.nodes[filename] = { "node": rdir._nodes[filename] }

        for filename, child in rdir.children():
            self.children[filename] = child
            self.children[filename]["branch"] = RawFolder(dir + "/" + filename)

    def lazyContain(self):
        if self.contain:
            return
        self.contain = True

        self.children = {}
        self.nodes = {}
        self.root = self.buildDir(self.dir)

rootNode = RawDirectory(root)
rootNode.lazyContain()

for filename in rootNode.children():
    print(filename.filename)

#
# === Agile plan:
#
# We might implement caching and other handling in later versions, where we need to
# optimize - tree.md locations could be cached and the API for the filesystem built
# by other means; files could be watched and their changes noticed. Database could
# be used. The result would be accessible via Anytree, and that's what we are interested
# in: we implement this interface on a low-optimum basis. Let's hope that file tree
# cache works and hard drive is still read once :)
#
# One we update to faster version, the simpler should be maintained as an implementation
# example, where we are interested in keeping the "open source" terms in access to minimal,
# readable and usable version, which can be optimized later as well.
#
# Notice that there are multiple ways of how this could be optimized: perhaps, we would
# implement different ways and create AI cards so that an AI would learn to build this
# system in multiple manners; for example some people would turn off tree.md mapping
# an put their code mostly into a subfolder or have other, separate function to map
# it somewhere. I think this could be achieved even in Apache, directly.
#
# Because we are creating a common standard for Laegna documentations: in case it would
# become a community effort at all, we would have multiple implementations of this format.
#
