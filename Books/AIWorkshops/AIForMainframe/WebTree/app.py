# = Flask Interface for Melted File Tree =
#
# This file implements a Flask interface built on top of an existing file tree mapper.
# It defines a class to "melt" together files with the same base name (ignoring extensions),
# folders with the same name, and nested backlink groups (from @@ blocks) into a unified group.
#
# The interface supports multiple output views (HTML, DHTML, JSON, or raw source) and allows
# parser plugins to be registered. Parser plugins convert source files (e.g. .py, .sh) into
# a version appended with ".htm" or ".html" for rendering.
#
# You can follow the original tasks by extending the merging logic, parser registrations, and hooks.

from flask import Flask, render_template, jsonify, request
import os

# = MeltedTreeFlaskInterface Class =
#
# This class builds on top of an existing file tree mapper (provided as "mapper") to create
# melted groups from files and folders that share the same base name and to nest backlinking pages.
class MeltedTreeFlaskInterface:
    """
    MeltedTreeFlaskInterface provides an API to process the prebuilt file tree,
    merge nodes with the same base identifier, and render a unified view.
    """
    def __init__(self, file_tree_mapper):
        """
        Initialize with an instance of FileTreeMapper.
        """
        self.mapper = file_tree_mapper
        self.parsers = {}  # Mapping from file extension (e.g. ".py") to parser functions.
        self.priority_hook = None
        self.garbage_collector_hook = None

    def register_parser(self, extension, parser_func):
        """
        Register a file parser for a specific file extension.
        The parser function should have the signature: parser_func(source_path, output_type)
        and return the processed content.
        """
        self.parsers[extension] = parser_func

    def set_priority_hook(self, hook_func):
        """
        Set the hook function to adjust chapter ordering or merging priorities.
        """
        self.priority_hook = hook_func

    def set_garbage_collector_hook(self, hook_func):
        """
        Set a hook for garbage collecting overly nested chapters.
        """
        self.garbage_collector_hook = hook_func

    def melted_group(self, link):
        """
        Given a URL link, find the corresponding node in the file tree,
        then merge together nodes (files, folders, backlinks) with the same base name.
        Returns a nested dictionary representing the melted group.
        """
        base_node = self.mapper.get_node_by_web_url(link)
        if not base_node:
            return None
        melted = self._melt_nodes(base_node)
        return melted

    def _melt_nodes(self, base_node):
        """
        Internal method to merge sibling nodes with the same base name
        and nest backlink items.
        (The merging logic here is a placeholder and should be refined per your requirements.)
        """
        melted_group = {
            "base_name": os.path.splitext(base_node.name)[0],
            "items": [],         # This list would be populated with merged nodes.
            "chapters": base_node.chapters  # Starting chapters from the primary node.
        }
        # TODO: Implement the detailed merging algorithm (merging files, folders, and @@ backlinks).
        return melted_group

    def render_view(self, link, view_type="html"):
        """
        Render the melted group for a given URL link in the specified view type.
        Supported view types: "html", "dhtml", "json", or "source".
        Returns an appropriate Flask response.
        """
        group = self.melted_group(link)
        if not group:
            return "Not Found", 404
        
        # Process each item in the group through a registered parser if available.
        for item in group["items"]:
            ext = os.path.splitext(item["name"])[1].lower()
            if ext in self.parsers:
                item["processed_content"] = self.parsers[ext](item["source_path"], view_type)
        
        # Apply hooks if defined.
        if self.priority_hook:
            group = self.priority_hook(group)
        if self.garbage_collector_hook:
            group = self.garbage_collector_hook(group)
        
        # Render according to the specified view type.
        if view_type == "json":
            return jsonify(group)
        elif view_type in ("html", "dhtml"):
            # In a full implementation, use templates. Here, we'll use a simple HTML string.
            return f"<html><body><h1>Melted View: {group['base_name']}</h1></body></html>"
        elif view_type == "source":
            return str(group)
        else:
            return "Unsupported view type", 400

# = Flask Application Setup =
#
# Set up the Flask application, instantiate the interface, register example parsers,
# and define a route to serve the melted view.
app = Flask(__name__)

# Assume 'mapper' is an instance of FileTreeMapper built earlier from your file tree.
mapper = None   # <-- Replace with your actual FileTreeMapper instance.
melted_interface = MeltedTreeFlaskInterface(mapper)

# = Example Parser Registration =
#
# Here we register a dummy parser for Python files, converting them into a markdown code block.
def py_to_md_parser(source_path, view_type):
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()
    md_content = "```python\n" + content + "\n```"
    return md_content

melted_interface.register_parser(".py", py_to_md_parser)

# = Flask Route for Melted View =
#
# The route below receives a file path (as "link") and an optional query parameter ("view")
# specifying the output view type. It renders the corresponding melted group.
@app.route("/view/<path:link>")
def view_file(link):
    view_type = request.args.get("view", "html")
    return melted_interface.render_view(f"/{link}", view_type=view_type)

# = Main Runner =
#
# Run the Flask app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
