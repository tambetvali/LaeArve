# Application Manual for LaegnaMath Website Widget

This manual explains the key features and setup instructions for the multi-view Flask application built with the LaegnaMathWebsiteWidget class. The application takes a single Markdown source and produces multiple views with download options.

## Supported Views

- **DHTML (.html):** Dynamic HTML view with interactive elements.
- **HTML (.htm):** A static, simple HTML view.
- **Markdown View (.md.htm / .md):**
  - Active Markdown rendering (using Mistune with syntax highlighting).
  - Downloadable source file (as .md).
- **JSON View (.json.htm / .json):**
  - Highlighted JSON view (rendered as a code block).
  - Downloadable raw JSON (as .json).
- **Python View (.py.htm / .py):**
  - Python code highlighted with Pygments in a Markdown-like view.
  - Downloadable raw Python source (as .py).

A dropdown menu (activated via a ☰ button in the top-right) lets users switch between these views and includes download buttons for the source files.

## How the Page Widget Class Works

The LaegnaMathWebsiteWidget class performs the following:
1. **View Generation:** Determines which view to render by examining the file extension in the URL.
2. **Pre-Jinja Processing:** Executes pre-processing scripts before running Jinja templates. The Markdown page doubles as both content and a template, and it may contain embedded Python code.
3. **Mistune Rendering:** Processes the Markdown via Mistune, allowing Python code to inject metadata into blocks. The metadata is later used in the JSON view.
4. **Final Output:** Renders the final view based on the format requested (HTML, DHTML, Markdown, JSON, or Python).

## Project Setup

1. **Directory Structure:**
   - Place the Flask application code in `app.py`.
   - Place the page widget class in `widget.py`.
   - Save the Bash script as `start.sh` in the project root.
   - Create a folder named `data_docs` for your Markdown source files (e.g., `example.md`).

2. **Installation and Startup:**
   - Create the Bash script with installation and startup commands (see start.sh below).
   - Create the Python files (app.py and widget.py) as provided.
   - In your terminal (in the project root), run the Bash script:
     
     chmod +x start.sh  
     ./start.sh
     
   - Open your browser at http://127.0.0.1:5000/ to view the application.

3. **View Behavior:**
   - The application selects a view based on URL parts (".html" for DHTML, ".htm" for HTML, ".md.htm" for active Markdown, ".md" for Markdown download, ".json.htm" for highlighted JSON, ".json" for JSON download, ".py.htm" for highlighted Python, and ".py" for Python download).
   - The top-right menu allows view switching and triggering downloads of the raw sources.

Use this manual to integrate the code below into your project.
