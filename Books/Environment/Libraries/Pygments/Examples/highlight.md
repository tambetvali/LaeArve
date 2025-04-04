# Flask and Pygments: Syntax Highlighting for Python and Markdown Examples

## Flask and Pygments Syntax Highlighting Example

This application utilizes Flask for its web server and Pygments for syntax highlighting. The page displays Python code as a formatted code block and includes links for both Python and Markdown examples.

1. **Application Structure**:
   - A single file contains all the necessary code to run the Flask application.
   - Two code strings (`python_code` and `markdown_code`) are predefined to represent the content for syntax highlighting.

2. **Core Functionality**:
   - Pygments processes the code strings using `highlight()` and renders them as HTML with syntax highlighting.
   - Flask serves the highlighted content via three routes: the homepage, a Python example page, and a Markdown example page.

3. **Routes**:
   - `/`: Displays Python code with syntax highlighting and links to other examples.
   - `/python`: Specifically highlights the Python code example.
   - `/markdown`: Specifically highlights the Markdown code example.

4. **Styling**:
   - Pygments' `HtmlFormatter` generates CSS for the syntax-highlighted code, ensuring the formatted blocks are visually appealing.

5. **User Interaction**:
   - Users can navigate between pages using links provided on the homepage.

## Running the Application

To execute the application:
1. Save the provided Python code into a file (e.g., `app.py`).
2. Run the file using `python app.py`.
3. Open a browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Why Use Flask and Pygments Together?

Flask provides the flexibility to design dynamic web applications, while Pygments excels in formatting and syntax highlighting. Together, they enable developers to create robust applications that showcase code examples with professional styling.
