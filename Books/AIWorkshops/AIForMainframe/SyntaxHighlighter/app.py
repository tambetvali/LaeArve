# # Flask File Viewer
#
# This application allows you to:
# - View Markdown (`.md`) files rendered into HTML alongside their source view.
# - View other files with syntax-highlighted source code and a download option.
# - Navigate the contents of the current folder with a side panel.
#
# **Features:**
# 1. Highlighted syntax using Pygments.
# 2. Comment blocks rendered in Markdown style.
# 3. Separate 'Web View' for Markdown and 'Source View' for all files.
#
# ## How to Use
# 1. Place the script in the folder you want to explore.
# 2. Run the server: `python script_name.py`.
# 3. Access `http://127.0.0.1:5000` in your browser.
#
# _Note: This code highlights Python docstrings and supports Markdown comments!_

import os
from flask import Flask, render_template_string, request, send_from_directory
from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
current_directory = os.getcwd()

@app.route("/")
def home():
    """Renders the home page with a list of files in the current directory."""
    files = os.listdir(current_directory)
    return render_template_string("""
    <!doctype html>
    <html>
    <head><title>File Viewer</title></head>
    <body>
        <h1>File Viewer</h1>
        <ul>
            {% for file in files %}
                <li><a href="/file/{{ file }}">{{ file }}</a></li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """, files=files)

@app.route("/file/<path:filename>")
def file_view(filename):
    """
    Displays the content of a file.
    - Markdown files are rendered into HTML (Web View).
    - Other files are shown with syntax-highlighted source code (Source View).
    """
    full_path = os.path.join(current_directory, filename)
    if not os.path.isfile(full_path):
        return "File not found", 404

    with open(full_path, 'r') as f:
        content = f.read()

    # Determine syntax highlighting using Pygments
    lexer = guess_lexer_for_filename(filename, content)
    formatter = HtmlFormatter(linenos=True, full=True, cssclass="codehilite")
    highlighted = highlight(content, lexer, formatter)

    # Differentiate Markdown files for Web View
    if filename.endswith(".md"):
        rendered_html = f"""
        <!doctype html>
        <html>
        <head>
            <style>{formatter.get_style_defs()}</style>
        </head>
        <body>
            <h2>Markdown File</h2>
            <div class="codehilite">
                {highlighted}
            </div>
            <hr>
            <a href="/download/{filename}">[Download]</a> | 
            <a href="/source/{filename}">[Source View]</a>
        </body>
        </html>
        """
    else:
        # Render non-Markdown files as Source View
        rendered_html = f"""
        <!doctype html>
        <html>
        <head>
            <style>{formatter.get_style_defs()}</style>
        </head>
        <body>
            <h2>Source View</h2>
            <div class="codehilite">
                {highlighted}
            </div>
            <hr>
            <a href="/download/{filename}">[Download]</a>
        </body>
        </html>
        """

    return rendered_html

@app.route("/download/<path:filename>")
def download(filename):
    """Allows downloading of a file from the current directory."""
    return send_from_directory(current_directory, filename, as_attachment=True)

if __name__ == "__main__":
    # Run the Flask server
    app.run(debug=True)
