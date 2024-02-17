from flask import Flask, request, jsonify
from flasktmpl import LaegnaNumberPageTemplate
from flasknumberwidget import LaegnaNumberWidget

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    # Create a new instance of the LaegnaNumberPageTemplate class with the appropriate title and subtitle
    template = LaegnaNumberPageTemplate(
        "Laegna Math Studies.",
        "Introducing the power of laegna numbers!"
    )
    
    # Add widgets or functionality as needed
    template.add_to_menu("/numbers?count=5", "Numbers")
    template.set_body("This is a page about laegna numbers for AI and human student.")
    template.add_widget(LaegnaNumberWidget(request.args))
    
    # Generate the HTML, JSON, or Markdown version of the page based on the requested format
    if request.args.get("format") == "markdown":
        return template.generate_markdown()
    elif request.args.get("format") == "json":
        return jsonify(template.generate_json())
    else:
        return template.generate_html()

@app.route("/numbers", methods=["GET"])
def numbers():
    # Create a new instance of the LaegnaNumberPageTemplate class with the appropriate title and subtitle
    template = LaegnaNumberWidget(request.args)
    
    # Add widgets or functionality as needed
    if request.args.get("format") == "html":
        return template.generate_html()
    elif request.args.get("format") == "json":
        return jsonify(template.generate_json())
    elif request.args.get("format") == "markdown":
        return template.generate_markdown()
    elif request.args.get("format") == "links":
        return jsonify({"links": template.generate_links()})
    else:
        # Default to HTML format if no format is specified
        return template.generate_html()
