from flask import Flask, render_template_string, request, url_for
from pygments import highlight
from pygments.lexers import PythonLexer, MarkdownLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

# Sample Python and Markdown code strings
python_code = '''def hello_world():
    print("Hello, World!")

def add(a, b):
    return a + b
'''

markdown_code = '''# Markdown Example

This is a heading

- Item 1
- Item 2

def sample_function(): return "Sample"
'''

def render_code(code, lexer):
    """Generate syntax-highlighted HTML from code."""
    formatter = HtmlFormatter(cssclass="highlight")
    highlighted_code = highlight(code, lexer, formatter)
    style = HtmlFormatter().get_style_defs('.highlight')
    return f"<style>{style}</style>{highlighted_code}"

@app.route('/')
def home():
    # Default view displaying Python code
    highlighted_python = render_code(python_code, PythonLexer())
    python_link = url_for('python_example')
    markdown_link = url_for('markdown_example')
    return render_template_string(f"""
    <h1>Welcome to the Code Highlighting Page</h1>
    <div>
        <h2>Python Code Example:</h2>
        {highlighted_python}
    </div>
    <div>
        <h3>Examples:</h3>
        <ul>
            <li><a href="{python_link}">Python Example</a></li>
            <li><a href="{markdown_link}">Markdown Example</a></li>
        </ul>
    </div>
    """)

@app.route('/python')
def python_example():
    highlighted_python = render_code(python_code, PythonLexer())
    return render_template_string(f"""
    <h1>Python Code Example</h1>
    <div>{highlighted_python}</div>
    <a href="/">Back</a>
    """)

@app.route('/markdown')
def markdown_example():
    highlighted_markdown = render_code(markdown_code, MarkdownLexer())
    return render_template_string(f"""
    <h1>Markdown Example</h1>
    <div>{highlighted_markdown}</div>
    <a href="/">Back</a>
    """)

if __name__ == '__main__':
    app.run(debug=True)
