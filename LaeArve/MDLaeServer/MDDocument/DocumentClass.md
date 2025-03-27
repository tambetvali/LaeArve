# Class Document

This is the Document Class of Laegna Web Server - the structured Document it's serving. It can convert from Document to Json and Back.

Json files are handled in format of String.

```python
class Chapter:
    def __init__(self):
        self.blocks = []
    
    def addBlock(self, type):
        block = {}
        block["type"] = type
        block["subblocks"] = []
        self.blocks.append(block)
        # So that content can be added inside:
        return block

class Document:
    def __init__(self, json):
        self.reset()
        self.readJson(json)
    
    self.reset(self):
        self.header = {}
        self.menu = []
        self.content = []
        self.tools = []
        self.references = []
    
    self.readJson(self):
        pass

    self.writeJson(self):
        pass

    # Getters for header, menu, content, tools and references
    # in format getHeader(), getMenu(), ...
```

## Parser for Chapter Tree

Document is made of the following main structural elements:
- Document
  - Subdocuments
  - Nested Documents

