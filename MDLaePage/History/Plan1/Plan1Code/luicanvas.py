from flask import Flask, render_template
import json

class LaegnaPageTemplate:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle

    def add_to_menu(self, link, title):
        self.menu.append((link, title))
    
    def set_body(self, body):
        self.body = body
    
    def add_widget(self, widget):
        self.widgets.append(widget)
    
    def generate_html(self):
        return render_template("laegna_numbers.html", title=self.title, subtitle=self.subtitle, menu=self.menu, body=self.body, widgets=self.widgets)
    
    def generate_json(self):
        json_data = {
            "title": self.title,
            "subtitle": self.subtitle,
        }
        return json.dumps(json_data)
    
    def generate_markdown(self):
        markdown = "# {title}\n{subtitle}\n\n".format(title=self.title, subtitle=self.subtitle)
        for menu in self.menu:
            markdown += " - [{link}]({link})\n".format(link=menu[0])
        return markdown + "\n" + self.body
