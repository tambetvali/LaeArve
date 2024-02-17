#
# This is the Laegna Math Spider meant to train an AI with Laegna Math Studies website.
#   It should be used by client and server.
#

# For LaeParam classes:
# - aspect = "server" if the parameters are initialized by and within server
# - aspect = "client" if the widgets (html aspect) / properties (json aspect) have been fetched
#   by browser (HTML, Json), or the Spyder (Json)
# - The widgets are not fetched by Markdown in browser, instead the user preconfigures the POST
#   parameters and as we don't have many GET parameters, each is passed in non-modified form when
#   we click the links; Markdown does not contain menus, buttons, selectors and web-specific elements,
#   and while it contains links, the link url is always given verbosely after the link itself.

# Classificator: provides an user with a list of selections to choose from.
#   HTML and dynamic HTML versions of the Laegna System will provide the following access:
#   - Dropdown menu
#   - Radio button set
#   Markdown is able to recognize the selections in links, but it's the printable version
#     and dynamic options must be done in HTML before switching to Markdown.
#   Json version will provide, along with it's Menu:
#   - Classificator selection list as Menu element
# Display of Classificators
class LaeParamClassificatorOrSet:
    def __init__(self, name, label = "", aspect = "server"):
        self.setName(name, label)
        self.selections = {}

    def setName(self, name, label = ""):
        # The identifier to access this variable
        #   Variable name is unique identifier through all the website, where:
        #   - GET method is link-based and does not remember the selections.
        #   - POST method stores the selection in server, for both Json (AI) and Html (User)
        #   - This holds for every container like Classificator, Set or String
        self.name = name
        # The label for this variable; if empty, the label is not used
        self.label = label
    
    def addSelection(self, name, label = ""):
        self.selections[name] = { "name": name, "label": label }

class LaeParamClassificator(LaeParamClassificatorOrSet):
    def __init__(self, name, label = "", display = "Dropdown", aspect = "server"):
        super.__init__(name, label)
        self.setDisplay(display)
    
    # Classificator has two displays:
    # - Dropdown: the default, display = "Dropdown"
    # - Radio set: the alternative, display = "Radio"
    # - Both displays differ, for our code, only in the content of this string and not in
    #   their behaviour.
    # Json version does not use the variable "display", but gives a list of selections,
    #   such as {name: name, label: label, selections: list of selection}
    # Json version feedback: in Python, GET and POST, selection is used as a string
    def setDisplay(self, display = "Dropdown"):
        self.display = display

class LaeParamSet(LaeParamClassificatorOrSet):
    def __init__(self, name, label = "", aspect = "server"):
        super.__init__(name, label)

    # Set has one display: a list of checkboxes.
    # Json version: {name: name, label: label, selections: list of selection}
    # Json version feedback: in GET and POST, it's encoded set, and in Python - a Set of names, strings

class LaeParamString:
    def __init__(self, name, label = ""):
        self.setName(name, label)
        self.selections = {}

    def setName(self, name, label = ""):
        self.name = name
        self.label = label

class LaeLink:
    def __init__(self):
        pass



class LaeJson:
    def __init__(self):
        pass