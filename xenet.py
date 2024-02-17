import den
import ten
import tene
import tenet

# This is the website navigation module, it would have pages for number types, lists and specific Q&A
# cards or documentation pages.

class NumberTypes:
    def __init__(self):
        self.registerTypes()

    def addType(self, name, cls):
        self.types[name] = cls

    def registerTypes(self):
        self.addType("Den", den.Den)
        self.addType("Ten", den.Den)
        self.addType("Tene", den.Den)
        self.addType("Tenet", den.Den)
