from flask import Flask, render_template
import json

# number_generation.py
def generate_numbers(count):
    numbers = []
    for i in range(1, count+1):
        numbers.append(i)
    return numbers

# LaegnaNumberWidget.py
class LaegnaNumberWidget():
    def __init__(self, request.args):
        self.title = "Laegna Numbers"
        self.subtitle = "A widget for displaying laegna numbers"
    
    def generate_html(self):
        return render_template("laegna_numbers.html", title=self.title, subtitle=self.subtitle)
    
    def generate_json(self):
        json_data = {
            "title": self.title,
            "subtitle": self.subtitle,
            "numbers": generate_numbers(5),
        }
        return json.dumps(json_data)
    
    def generate_markdown(self):
        markdown = "# {title}\n{subtitle}\n\n".format(title=self.title, subtitle=self.subtitle)
        for number in self.numbers:
            markdown += " - [{number}](/numbers/{number})\n".format(number=number)
        return markdown + "\n"
    
    def generate_links(self):
        links = []
        for number in self.numbers:
            links.append("/numbers/{number}".format(number=number))
        return links
