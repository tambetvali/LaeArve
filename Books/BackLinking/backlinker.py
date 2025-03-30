

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
