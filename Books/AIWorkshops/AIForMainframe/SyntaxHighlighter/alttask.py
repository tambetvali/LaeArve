import re
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.token import Comment, String
from pygments import highlight
from pygments.formatters import HtmlFormatter
import mistune


class CodeProcessor:
    """
    A class to use Pygments and Mistune for processing code files.
    """
    def __init__(self):
        """
        Initialize CodeProcessor and create a list of supported languages.
        """
        self.supported_languages = {
            name: ext
            for name, aliases, exts, mimetypes in get_all_lexers()
            for ext in exts
        }

    def get_supported_languages(self):
        """
        Get the extensions and names of supported languages.

        Returns:
            dict: A dictionary with language names and extensions.
        """
        return self.supported_languages

    def extract_comments(self, code, lexer_name):
        """
        Extract all comments from the code along with their positions.

        Args:
            code (str): The source code.
            lexer_name (str): The name of the lexer to use.

        Returns:
            list: A list of dictionaries containing comments and their positions.
        """
        lexer = get_lexer_by_name(lexer_name)
        tokens = lexer.get_tokens(code)
        comments = []
        position = 0

        for token_type, value in tokens:
            if token_type in Comment:
                # Store the comment and its start position
                comments.append({
                    "comment": value.strip(),
                    "start_position": position,
                    "end_position": position + len(value)
                })
            position += len(value)

        return comments

    def highlight_code_with_api_strings(self, code, lexer_name):
        """
        Highlight code and emphasize API docstrings (Python-style).

        Args:
            code (str): The source code.
            lexer_name (str): The name of the lexer to use.

        Returns:
            str: HTML-rendered syntax-highlighted code.
        """
        lexer = get_lexer_by_name(lexer_name)
        formatter = HtmlFormatter(linenos=True, cssclass="codehilite")

        # Highlight the entire code
        highlighted_code = highlight(code, lexer, formatter)

        # Detect and emphasize API docstrings
        docstring_pattern = r'("""|\'\'\')([\s\S]*?)(\1)'
        highlighted_code = re.sub(
            docstring_pattern,
            lambda match: f"<mark>{mistune.create_markdown()(match.group(2))}</mark>",
            highlighted_code
        )

        return f"<style>{formatter.get_style_defs()}</style>{highlighted_code}"


# Example Usage
if __name__ == "__main__":
    processor = CodeProcessor()

    # Example: Retrieve supported languages
    print("Supported Languages:")
    for lang, ext in processor.get_supported_languages().items():
        print(f"{lang}: {', '.join(ext)}")

    # Example: Extract comments
    sample_code = """
    # This is a sample comment
    def foo():
        \"\"\"API docstring example.\"\"\"
        print("Hello, World!")  # Another comment
    """
    comments = processor.extract_comments(sample_code, "python")
    print("\nExtracted Comments:")
    for comment in comments:
        print(comment)

    # Example: Highlight code with API strings emphasized
    html_output = processor.highlight_code_with_api_strings(sample_code, "python")
    with open("highlighted_code.html", "w") as f:
        f.write(html_output)
