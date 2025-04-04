import os
import re
import json
from jinja2 import Environment, FileSystemLoader
import mistune
from pygments import highlight
from pygments.lexers import MarkdownLexer, JsonLexer, PythonLexer
from pygments.formatters import HtmlFormatter

class LaegnaMathWebsiteWidget:
    def __init__(self, md_file_path, view_format='dhtml'):
        self.md_file_path = md_file_path
        self.view_format = view_format
        self.md_source = self.load_markdown()
        self.blocklist = {}
        self.process_phases = ["template", "processing", "finalize"]

    def load_markdown(self):
        """Load the Markdown source from the file."""
        if os.path.exists(self.md_file_path):
            with open(self.md_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return "# No content found"

    def get_markdown_source(self):
        """Return the original Markdown source."""
        return self.md_source

    def get_python_source(self):
        """Return the Python source; implement extraction as needed."""
        return "# Python source extraction not implemented."

    def parse_jinja_blocks(self):
        """
        Parse Jinja2 template blocks from the Markdown.
        Blocks are delimited by lines such as:
        "# § run, role=template" and "# § end".
        """
        pattern = re.compile(r'# § run[,;]\s*role=(\w+)(.*?)# § end', re.DOTALL)
        matches = pattern.findall(self.md_source)
        templates = {}
        for role, content in matches:
            templates[role.strip()] = content.strip()
        return templates

    def run_template_phase(self):
        """Perform pre-Jinja processing and execute embedded Jinja templates."""
        env = Environment(loader=FileSystemLoader(os.path.dirname(self.md_file_path)))
        template = env.from_string(self.md_source)
        rendered = template.render()
        self.md_source = rendered
        self.blocklist['template_executed'] = True

    def run_processing_phase(self):
        """Execute additional processing on the Markdown (e.g., code block execution)."""
        self.blocklist['processed'] = True

    def run_finalize_phase(self):
        """Finalize the page by making final corrections."""
        self.blocklist['finalized'] = True

    def get_json_data(self):
        """Return the internal state and content as a JSON object."""
        data = {
            "blocklist": self.blocklist,
            "content": self.md_source
        }
        return data

    def render_markdown(self):
        """Render Markdown to HTML and include a syntax-highlighted view of the source."""
        html = mistune.markdown(self.md_source)
        lexer = MarkdownLexer()
        formatter = HtmlFormatter()
        highlighted = highlight(self.md_source, lexer, formatter)
        combined = (
            "<div class='markdown-render'>" + html + "</div>"
            "<hr/><div class='markdown-highlight'>" + highlighted + "</div>"
        )
        return combined

    def render_html(self):
        """Render a simple HTML view."""
        return "<div class='html-view'>" + self.md_source + "</div>"

    def render_dhtml(self):
        """
        Render a DHTML view that includes an interactive menu (with a ☰ button)
        and dual panels for the menu and content.
        """
        menu_html = self.render_menu()
        content_html = self.render_markdown()
        dhtml_template = (
            "<html><head><title>DHTML View</title><style>"
            "body { font-family: Arial, sans-serif; margin: 0; padding: 0; }"
            "#menu-button { position: absolute; top: 10px; right: 10px; font-size: 24px; cursor: pointer; }"
            "#menu-panel { display: none; position: absolute; top: 40px; right: 10px; background: #f9f9f9; border: 1px solid #ccc; padding: 10px; z-index: 1000; }"
            "#content-panel { padding: 20px; }</style>"
            "<script>"
            "function toggleMenu() { var menu = document.getElementById('menu-panel');"
            "menu.style.display = (menu.style.display === 'none' || menu.style.display === '') ? 'block' : 'none'; }"
            "</script></head><body>"
            "<div id='menu-button' onclick='toggleMenu()'>☰</div>"
            "<div id='menu-panel'>" + menu_html + "</div>"
            "<div id='content-panel'>" + content_html + "</div>"
            "</body></html>"
        )
        return dhtml_template

    def render_json(self):
        """Render JSON data with syntax highlighting."""
        json_data = json.dumps(self.get_json_data(), indent=4)
        lexer = JsonLexer()
        formatter = HtmlFormatter()
        highlighted = highlight(json_data, lexer, formatter)
        json_template = (
            "<html><head><title>JSON View</title><style>" +
            formatter.get_style_defs('.highlight') +
            "</style></head><body><div class='json-view'>" +
            highlighted + "</div></body></html>"
        )
        return json_template

    def render_python(self):
        """Render Python code with syntax highlighting."""
        source = self.get_python_source()
        lexer = PythonLexer()
        formatter = HtmlFormatter()
        highlighted = highlight(source, lexer, formatter)
        python_template = (
            "<html><head><title>Python View</title><style>" +
            formatter.get_style_defs('.highlight') +
            "</style></head><body><div class='python-view'>" +
            highlighted + "</div></body></html>"
        )
        return python_template

    def render_menu(self):
        """Render the top-right menu with view and download links."""
        menu_items = [
            "<a href='?view=html.htm'>HTML</a>",
            "<a href='?view=dhtml.html'>DHTML</a>",
            "<a href='?view=markdown.md.htm'>Markdown</a>",
            "<a href='?view=json.json.htm'>JSON</a>",
            "<a href='?view=python.py.htm'>Python</a>",
            "<a href='?view=anki.htm'>Anki</a>",
            "<a href='?view=folder.htm'>Folder</a>",
            "|",
            "<a href='?view=markdown.md.htm&download=1'>Download Markdown</a>",
            "<a href='?view=json.json.htm&download=1'>Download JSON</a>",
            "<a href='?view=python.py.htm&download=1'>Download Python</a>"
        ]
        return " ".join(menu_items)

    def render(self):
        """
        Execute processing phases (template, processing, finalize)
        and then render the view based on the requested format.
        """
        self.run_template_phase()
        self.run_processing_phase()
        self.run_finalize_phase()

        if self.view_format in ['markdown', 'md']:
            return self.render_markdown()
        elif self.view_format == 'html':
            return self.render_html()
        elif self.view_format == 'dhtml':
            return self.render_dhtml()
        elif self.view_format == 'json':
            return self.render_json()
        elif self.view_format in ['python', 'py']:
            return self.render_python()
        else:
            return self.render_dhtml()
