
import mistune
md = mistune.create_markdown()

with open("index.md", 'r') as file:
    md_content = file.read()

content = """

# header 1

A block.

"""

bs = mistune.BlockState()
parsed, bs = md.parse(content)

bs.add_paragraph("Testes")

bs.tokens.

#print(mistune)

print(rnd)

class BackLinker:
    def __init__(self):
        self.treeitems = {}

        # Appear inside the next section
        self.forward_links = []

        # Appear inside the last section,
        # backwards; for example into the
        # previous paragraph. They appear
        # reversed.
        self.backward_links = []
    
    # Chapter without reference, outside not
    # accessible; do not allow links except
    # "#"-inpage positioning and pager page.
    def append(self, value):
        n = 0

        
        
a = BackLinker()
a.append("apple")
a.append("tree")
