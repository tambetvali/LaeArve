from bases import DigitBase
from octaves import ROctave
from dim import 

# Mirror would give a view to the number, where one can view the same number with different:
# - Type is "NUM", "TXT", "HTML", "JSON", "SVG"
class Mirror:
    def __init__(self, dialect):
        self.dialect = dialect
        self.type = "NUM"

    def setVisibilityFlags(self, type = "NUM"):
        self.type = type
    
    def represent(self, type = None):
        # If type is not given, use the configuration to represent a number
        if type == None:
            type = self.type

    def str(self):
        type = self.type
        # We are not able to return numbers
        if type == "NUM":
            type = "TXT"
        return self.represent(self, type)

class NumberSystemDialect(Mirror):
    def __init__(self) -> None:
        self.base = DigitBase()
        self.roctave = ROctave()

