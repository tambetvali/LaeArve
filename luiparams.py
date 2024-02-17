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

# Possible types:
# type="string"
# type="integer"
# type="float"
class LaeParamString:
    def __init__(self, name, label = "", type = "string", aspect = "server"):
        self.setName(name, label)
        self.selections = {}

    def setName(self, name, label = ""):
        self.name = name
        self.label = label

# ParameterBox: pages can have their parameter boxes;
#   currently - let's have only GET parameter boxes and let's ignore POST in the manual, each link
#     just carries all the parameters, whether or not used locally (use param prefix to identify),
#     so just safely ignore where I mention POST - POST is simply possible but right now I won't
#     implement.
class LaeParameterBox:
    def __init__(self, label = "Parameters"):
        self.params = []
    
    # Aspect is server for serving pages, such as Json or Html; or client if it's the Spider.
    # name is the name of the parameter, included in link, hidden in html, and dictionary key and first
    #    item in Json.
    # label is the visible name in HTML; it's also known in Json as "label" in the Json item.
    # display is either "Dropdown" or "Radio" in case of classificator
    # prange:
    #    it could be a range such as: 0:10 would create classificator or set with values between
    #    0 and 10, within the range, or number entry of being able to enter values in between,
    #    for string - which is then probably text type.
    #    it could be list of strings and numbers to be selected.
    #    it could be type of Numbers, Floats or Text, like type(String).
    #    for textbox, it could be None to allow anything available.
    def addParameter(self, name, value, display, type, prange, label = "", aspect = "server"):
        if type == "Classificator":
            # Display is either Dropdown or Radio
            classificator = LaeParamClassificator(name, label, display, aspect)
            classificator.setValue(value, prange)
            self.params.append()
        elif type == "Set":
            paramset = LaeParamClassificator(name, label, aspect)
            classificator.setValue(value, prange)
            self.params.append()
        elif type == "String":
            paramstring = LaeParamClassificator(name, label)
            classificator.setValue(value, prange)
 
class LaeConfigurator:
    def __init__(self):
        self.params = []

    def addParamBox(self, laeparambox):
        self.params.append(laeparambox)