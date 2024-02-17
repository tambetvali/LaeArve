# Letter class is used to display numeric and alphanumeric digits.
# It's resolving missing letters in font and other visual problems we might get.

# Notice that from accents, we are interested in implementing dot accent, accent up, accent down,
# and their double-versions to map into numeric system. Other accents are either high-order solutions
# or non-linear and their number values exist, but not as primitive math or basic math. We do not want
# to implement them from scratch or decimal system, but we want to have the basic Laegna calculus to
# define and _then_ implement them.
# To have this defined, our goal: to implement standard, strict and symmetric Laegna numbers as basis
# of our math, where to have high level behaviours such as acceleration outside it's numeric value is
# rather higher-level math, which could be slower, not so easy to implement and thus having additional
# complexities when mixed with trivia. For example Assembler is not supposed to know them.

from digitvalue import DigitValue
from testconf import *
import bases

Den0 = ["U"]
Denex0 = ["V"]
Den1real = ["OA"]
Den1imag = ["OA"]
Den2 = ["ST", "MN"]

Ten0 = ["UǗ"]
Tenex9 = ["VW"]
Ten1real = ["IOAE"]
Ten1imag = ["QPOR"]
Ten2 = ["GFEH", "CBAD", "QPOR", "KJIL"]

Op0 = ["·:"]
Op1 = ["/-+*"]

Dec0 = ["09"]
Dec1real = ["1234"]
Dec1imag = ["5678"]
Dec2 = ["1234", "5678"]

Ren0 = ["X"]
Ren1real = ["ZY"]
Ren1imag = ["ZY"]
# Notice that zero, here, has custom implementation - it's part of complex structure
# Ren2 is just an example that without zero, it would look like Den2; as zeroes are
# at both dimensions separately, the Ren2withzero is actually used.
Ren2 = ["13", "79"]
Ren2withzero = ["123", "456", "789"]

# Mirror is the general number type:
#   Indeed, it mirrors the number to itself, containing all the information we miss here; it's rather
#   explained by being the base class of NumberSystemDialect, and instance of the dialect is contained.
#   "Mirror" is the last word of display settings of the number, where the same number is mirrored as
#   being Json content, normal number, md (txt) or html code of it. Mirror.dialect, a neccessary variable
#   of it, allows to trace back to the actual type and settings of the number and then, LetterDictionary
#   can form a number representation based on the current view; the main representatives of a number
#   are Mirror and LetterDictionary. Well _Mirror_ _is_ a self-explanatory name!
class LetterDictionary:
    def __init__(self, type = "Ten", mirror = None):
        loghead("Initializing LetterDictionary, setting dimension to " + str(dimension) + " and " +
                "base to " + str(type) + " by default.")
        logsubhead("! Letter with dimension 1 and type Ten means normal, multidigit Tens.")
        self.setLetterType(type)
        self.setMirror(mirror)

    def setMirror(self, mirror = None):
        self.dialectMirror = mirror

    def setLetterType(self, type = "Ten"):
        self.letterType = type

    # dim: dimension is either 1 or 2, do you use only the real axe or both components of the complex.
    # One input digit, thus, if dim = 2, contains data about two letters.
    # digits: either one DigitValue or several DigitValues in a list.
    def getLetters(self, digits, dim = 1):
        if type(digits) == type(DigitValue):
            digit = digits
            digits = None
        if digits:
            letters = ""
            for digit in digits:
                letters += self.getLetter(digit, dim)
            return letters
        else:
            digit: DigitValue
            # Process the actual digit.
            if self.type == "Den":
                

class Dialect:
    def __init__(self, dimension = 1, type = "Ten"):
        loghead("Initializing LetterSet, setting dimension to " + str(dimension) + " and " +
                "base to " + str(type) + " by default.")
        logsubhead("! Letter with dimension 1 and type Ten means normal, multidigit Tens.")
        self.setLetterType(dimension, type)

    def setLetterType(self, dimension = 1, type = "Ten"):
        log("- DigitBase: setting dimension to " + str(dimension) + ", type to " +
            str(type) + ".")
        self.dimension = dimension
        self.type = type

    def getLetterType(self):
        log("- DigitBase: returning dimension " + str(self.dimension) + " with type " +
            str(self.type) + ".")
        return self.dimension, self.type

    def test(self):
        for testBase in range(0, 3):
            self.setBase(0)
            self.getBase()
            self.getBaseDim()
            log("User literal: " + str(self))

# Dimension, here, is not the full dimension, but how many letters there are in one letter - accents and
# other dimensions can be applied values dynamically and need not to be defined, as that number does not
# influence the letter content much and where it does, it should be detected automatically (for example
# space for the complex accents).
# Types:
# Den - generate one Den, pair of Dens etc., using the Den looks
# Ten - generate a Ten
# Op - generate a mathematical operation, such as division
# Dec - generate a decimal number of Laegna
# Ren - generate a coordinate space modificator (mantissa)
class Letter(Dialect):
    def __init__(self, dialect = None):
        self.dialect = dialect
        loghead("Initializing Letter, setting dialect to " + str(dialect))
        logsubhead("! Letter with dialect Ten is a basic letter type of multiple Ten digits.")
        self.reset()
    
    # Remove all properties of the letter, equivalent to generating a new letter, not touching
    # the type and dimension.
    def reset(self):
        self.digits = [None] * self.dimension
        self.accents = [[None, None, None, None, None, None, None, None]] * self.dimension

    def __str__(self):
        return self.getLetter()

testhead("= Initializing Dialects. =")
testsubhead("  _running tests (only output is generated for manual review)_")
test(Dialect)
testfoot("Dialect test finished.")