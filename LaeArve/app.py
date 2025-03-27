# This is the Flask Application, basically part of Laegna Math Framework, as it actually
# defines the API rather than any specific servie. Don't mind if you cannot follow my logic
# immediately - there is None.
# Laegna Math Documentation is following Logecs and Logecs Mathematecs. This means any sentence
# is rather ponegative than anything like Logical, so kick your ass if you find some logical
# mistakes like a big surprise; those surprises are just a first Lì and it might feel like Lè.
# (for there are many people, I cannot even write, who are very ex<i>c</i>ited about their dummy
# Logic)

from flask import Flask, render_template, url_for

app = Flask(__name__)

class Subpage(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content

subpages = [Subpage("Documents", "Hack around here."),
            Subpage("Books", "Learn what you can."),
            Subpage("Excercises", "Do your Fine Tuning.")]

@app.route("/")
def index():
    return render_template("index.html", subpages=subpages)

@app.route("/<name>")
def subpage(name):
    try:
        subpage = next(s for s in subpages if s.name == name)
    except StopIteration:
        return "Subpage not found."
    else:
        return render_template("subpage.html", title=subpage.name, content=subpage.content)