from flask import Flask, request, render_template
import markdownclient

app = Flask(__name__)

@app.route('/')
def index():
    files = [f for f in os.listdir('.') if f.endswith('.py')]
    return render_template('index.html', files=files)

@app.route('/<string:file>')
def show(file):
    parser = markdownclient.Parser()
    code = parser.parse(file)
    return render_template('show.html', file=code)
