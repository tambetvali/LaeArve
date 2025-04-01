from flask import Flask, render_template_string, request, url_for
import mistune

app = Flask(__name__)

# Sample content structure
markdown_text = """
### Chapter 1
#### Subchapter 1.1
##### Subchapter 1.1.1
###### Subchapter 1.1.1.1
####### Subchapter 1.1.1.1.1
######## Subchapter 1.1.1.1.1.1
#### Chapter 1.2
##### Subchapter 1.2.1

### Chapter 2
#### Subchapter 2.1
#### Subchapter 2.2
#### Subchapter 2.3
#### Subchapter 2.4
#### Subchapter 2.5
#### Subchapter 2.6

### Chapter 3
> A long block with more than 127 characters here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
> Another long block here with lots of text that would also count as a multiblock example.
"""

# Flask routing
@app.route("/")
def index():
    return render_page("Main Page", markdown_text, "main")

@app.route("/subpage/<page_id>")
def subpage(page_id):
    # Generate dynamic content for subpages
    content = f"### Subpage for {page_id}\n\nThis is additional content for the section '{page_id}'..."
    return render_page(f"Subpage - {page_id}", content, page_id)

# Helper functions
def process_markdown(content, page_id):
    """Processes Markdown with garbage collection rules and adds continue links."""
    parser = mistune.create_markdown()
    lines = content.splitlines()
    processed_content = []
    chapter_stack = []
    block_count = 0
    multi_block_count = 0

    for line in lines:
        stripped_line = line.strip()

        # Handle chapters starting from H3
        if stripped_line.startswith("###"):
            level = stripped_line.count("#")
            chapter_stack.append((level, stripped_line))
            if len(chapter_stack) > 5:
                # Add "continue" link and truncate
                continue_link = f"[Continue reading...]({url_for('subpage', page_id=page_id)})"
                processed_content.append(f"{chapter_stack[-6][1]}\n{continue_link}\n")
                chapter_stack = chapter_stack[:5]
            else:
                processed_content.append(stripped_line)

        # Handle excessive chapter lists
        elif stripped_line.startswith("####"):
            block_count += 1
            if block_count > 5:
                continue_link = f"[Continue to subpage...]({url_for('subpage', page_id=page_id)})"
                processed_content.append(f"{continue_link}")
                break
            else:
                processed_content.append(stripped_line)

        # Handle blocks
        elif stripped_line.startswith(">"):
            if len(stripped_line) > 127:
                multi_block_count += 1
            if multi_block_count > 40:
                continue_link = f"[Read more...]({url_for('subpage', page_id=page_id)})"
                processed_content.append(continue_link)
                break
            else:
                processed_content.append(stripped_line)

        else:
            processed_content.append(stripped_line)

    return "\n".join(processed_content)

def render_page(title, content, page_id):
    """Renders the HTML page with the processed Markdown content."""
    processed_content = process_markdown(content, page_id)
    html_content = mistune.create_markdown()(processed_content)
    return render_template_string("""
    <!doctype html>
    <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>{{ title }}</h1>
            <div>{{ content|safe }}</div>
        </body>
    </html>
    """, title=title, content=html_content)

if __name__ == "__main__":
    app.run(debug=True)
