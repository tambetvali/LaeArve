# LuiParams - Iteration 1

As an AI described my full task as a little complicated, I create a simplified structure here, so that we can replace the luiparams.py altogether and have a simplification - I think I understood what is complicated (an AI is generally good in telling about complications):

I don't implement any code, but only headers - I think an AI got complications with my code as it is, and if it's a structure too complicated, then at my age we don't want to mess with this.

## class LuiRange

``` python
# This is the automatically processable metadata, which can be added to types or values
class LuiMetadata:
    def __init__(self):
        self.metadata = {}
    
    def addMetadata(self, name, value):
        self.metadata[name] = value
    
    def addTag(self, name):
        # Here it behaves like a set, given hash tag is added
        self.metadata[name] = True

    # Make it iterable and accessible by name, so that it behaves like dictionary itself.
    # Over all of the system, metadata item with the same name is always the same

class LuiRange:
    def __init__(self, name, label = None, metadata = LuiMetadata()):
        self.name = name
        self.metadata = metadata
        self.label = label
        setString()

    def clone(self, name, label):
        # Create an instance with different name and label, but same initial condition.
        #   For inheritance: create more general range, and clone it to several more specific ranges.

    def setString(self, format = "String"):
        # This is String, Text, Number or Float; each has a string representation.
        self.type = "String"
        self.format = one of "String", "Text", "Number", "Float"
        self.multiselect = None
        # This adds metadata or later, autosuggestions
        self.values = {}
    
    def setClassificator(self, format = "Expanded", multiselect = False):
        # This is either single-selection or multiselection
        self.type = "Classificator"
        self.multiselect = multiselect
        # Expanded format has the selections visible at once, for Compressed format, one has to open
        # the list. It's up to implementation, how it's visualized and whether more styles are applied
        # to the widget outside this datatype.
        self.format = format
        # This is used for metadata and selectable items; it's an ordered dictionary, as current python
        # supports ordering dictionaries like lists, for example you can sort them.
        self.values = {}
    
    def addValue(self, name, label = {}, metadata = LuiMetadata()):
        self.values[name] = {"name": name, "label": label, "metadata": metadata}
    
    def setType(self, type, format, values, multiselect):
        # set all the values at once

    def getType():
        return (self.type, self.format, self.values, self.multiselect)

# Construct this for:
#   Spyder will use this to have access to properties. We have our own Spyder!
#   For Html and Markdown, metadata is not used at all.
#   Html menu will use this for side menu.
#   Markdown will generate short list of properties and also a link to the same widget at separate page
#   For Json, metadata is part of the object.
#   For text types value list is for autocomplete: initially not user, but an AI will complete text
#     field values, as well as Spyder. By AI we mean a program to use Spyder to train an AI.
#   In Json, 
class LuiEditableWidget:
    def __init__(self, rng: LuiRange = None, name = None):
        if rng == None and name == None: throw Exception() # Not enough inputs
        if name != None and name != rng.name: throw Exception() # Naming conflict
        if rng == None: rng = LuiRange(name) # Will be string without label
        self.name = rng.name if eng else name
        self.rng = rng
        self.value = None
    
    # Autocomplete is not allowed here, even if choosing a certain selection from dropdown could
    # disable an associated text box.
    def getStaticHtml(self):
        # Get compatible widget for editing text or number, or picking one or several selections
        # from the list, with label will be label and name will set the GET variable name.
    
    # This could have autocomplete; initial version might be "pass"
    def getDynamicHtml(self):
        pass

    def getJson(self):
        # Get the object with type, name, label, values, and metadata of the whole widget or the values
    
    def getMarkdown(self):
        # This is the simplest (but check if name and value are not None):
        return self.name + ":" + str(self.value)

class LabelWidget

class Properties:
    def __init__():
        self.blocks = []

    def addLabel(self, name, label, metadata: LuiMetadata):
        # Name and metadata: let's add them to groups for AI or Spyder.
        # For users, only label is visible.
        ...
        self.blocks.append(label)
    
    def addProperty(self, LuiEditableWidget):
        ...
        self.blocks.append(prop)

    # Static html is very plain and simple, but not completely static - for example, while we don't
    # want to use innerHtml, we might change the selection with JS; we could do this even with old
    # browsers - it's not very expensive.
    def getStaticHtml(self):
        # Create the margins, paddings, colors, borders, whatever the design would be (does not matter
        # in code much)
        # Get Labels and Properties as Html elements
        # For markdown, separate-page version exists so that "Properties" link allows to configure
        #   the page.

        # Can we somehow, still providing user with normal file, with content-type etc. get the
        # browser to show line feeds?
    
    # This autoupdates the page; initial version might be "pass"
    def getDynamicHtml(self):
        pass
    
    def getJson(self):
        # Get the dict / list of objects with metadata, where the dict itself has metadata as well,
        #   such as what you should do with this page anyway - is it text, Q&A, etc.
    
    def getMarkdown(self):
        # This is the simplest (but check if name and value are not None):
        md = Link("Properties", html_page)
        return self.name + ":" + str(self.value)

```