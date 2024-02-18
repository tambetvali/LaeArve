from dim import *

# Connect the little dimensional database of the number with computer
class ComputationalDimension:
    def __init__(self, source = None, sourceLink = None, base = 1, roctave = 1):
        self.dimensionid = dimensionSingleton.appendDimension(self)
        if source != None:
            # Add one source; this turns the dimension into read-only
            self.sources = [source]
            self.sourceLinks = [sourceLink]
        else:
            # Create a data container
            self.sources = [ComputationalTarget(base, roctave)]
            self.sourceLinks = self.sources[0].link()
        self.base = bases.DigitBase(base)
        self.roctave = octaves.ROctave(roctave)
    
    # It would be messy to have too much input for the __init__, so we add the rest of the links later.
    def addSourceLink(self, source, sourceLink):
        self.sources.append(source)
        self.sourceLinks.append(sourceLink)

    def getDen(self, number):
        den = ComputationalDimension(self, number, 2, self.roctave)

    def getId(self):
        return self.dimensionid

# This is the "source", which directly contains data and thus, is not read-only
class ComputationalTarget(ComputationalDimension):
    def __init__(self, base = 2, roctave = 1, number = 0):
        self.number = number
    
    # Return source links
    def link():
        return [1, 2]

# Here, digits get calculated
class ComputationalDigit:
    def __init__(self, dimension):
        self.dimension = dimension
    
    def getDigitValueAbsolute(self):
        return 

# I call positioned numbers "Strings", where in Laegna words and numbers share the same
# basic type to reflect the language philosophy in programming.
class ComputationalString:
    def __init__(self, dimension):
        self.dimension = dimension

# This is the Computer or Calculator for the number - it generally manages the interactions
#   between other components to simulate a number type; especially it sets up all dimensions
#   and connects them with actual calculators.
# The actual number as available from API (xene) will use the Computer to synchronize it's
#   states, activities and data types.
class Computer:
    def __init__(self, base = 1, roctave = 1):
        # Set up the base dimension of this _number computer_
        self.dimension = ComputationalDimension(base=base, roctave=roctave)
        # Set up the digit string for this number
        self.string = ComputationalString()
