from flask import Flask, request, jsonify, make_response
from widget import LaegnaMathWebsiteWidget
import os

app = Flask(__name__)

# Base Markdown file as source, located in the "data_docs" directory.
BASE_MD_FILE = os.path.join(os.path.dirname(__file__), 'data_docs', 'example.md')

@app.route('/')
def index():
    # Determine the view format from the query parameter; default is 'dhtml'
    view_format = request.args.get('view', 'dhtml').lower()
    
    # Choose file extension conventions based on view
    if view_format == 'dhtml':
        ext = '.html'
    elif view_format == 'html':
        ext = '.htm'
    elif view_format in ['markdown', 'md']:
        ext = '.md.htm'
    elif view_format == 'json':
        ext = '.json.htm'
    elif view_format in ['python', 'py']:
        ext = '.py.htm'
    else:
        ext = '.html'
    
    # Initialize the page widget
    widget = LaegnaMathWebsiteWidget(BASE_MD_FILE, view_format)
    rendered_content = widget.render()

    # Handle download requests if the "download" query parameter is present.
    download = request.args.get('download', None)
    if download:
        if view_format in ['markdown', 'md']:
            response = make_response(widget.get_markdown_source())
            response.headers["Content-Disposition"] = "attachment; filename=content.md"
            response.headers["Content-Type"] = "text/markdown"
            return response
        elif view_format == 'json':
            response = jsonify(widget.get_json_data())
            response.headers["Content-Disposition"] = "attachment; filename=content.json"
            return response
        elif view_format in ['python', 'py']:
            response = make_response(widget.get_python_source())
            response.headers["Content-Disposition"] = "attachment; filename=content.py"
            response.headers["Content-Type"] = "text/x-python"
            return response

    # Return the content with the proper MIME type
    if view_format == 'json':
        return rendered_content, 200, {'Content-Type': 'application/json'}
    else:
        return rendered_content

if __name__ == '__main__':
    app.run(debug=True)
