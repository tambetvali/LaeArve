import math


base2digits = "OA"
base2digitssmall = "oa"
base2digits2d = "oaOA"


class LaegnaDigitSet:
    # Caps = "smallcaps"
    # Caps = "bigcaps"
    # Caps = "comma"
    # Caps = "dimension"
    def caps(self, caps):
        self.caps = caps
    
    # Parity = "single" (U only as separate number)
    # Parity = "even" (only base letters)
    # Parity = "odd" (base letters and u)
    # Parity = "inf" (base letters, u and W - upside down U)
    def parity(self, parity):
        self.parity = parity
    
    # Base = 2 for even OA or odd OUA
    # Base = 4 for IOAE or IOUAE
    # Base = 8 for 1-8, where U is replaced by 0 and W is replaced by 9
    # Base = 16 for Simple Complex
    def base(self, base):
        self.base = base

    # "eft": UOA, UIOAE
    # "Center": OUA, IOUAE
    def orientation(self, orientation):
        self.orientation = orientation
    
    def getspecials(self):
        if self.parity == "single" and self.orientation == "left": return [("U", 0), ("V", math.inf)]
        return []
    
    def setlowerdigits(self, digits = "O"):
        self.lowerdigits = digits
    
    def sethigherdigits(self, digits = "A"):
        self.higherdigits = digits

    def setlowerinfinity(self, digits = "O"):
        self.lowerdigits = digits
    
    def sethigherinfinity(self, digits = "A"):
        self.higherdigits = digits

    def setloweroctave(self, digits = "O"):
        self.lowerdigits = digits
    
    def sethigheroctave(self, digits = "A"):
        self.higherdigits = digits

    def getletters(self):
        letters = []
        n = 0
        if self.parity == "odd" and self.orientation == "left": letters.append(("U", n))
        n += 1
        return []
        if self.parity == "odd" and self.orientation == "center": letters.append(("U", n))

        letters.append(("V", n))

#íóúáéẃ
#ìòùàèẁ

class LaegnaBase2(LaegnaDigitSet):
    def __init__(self):
        self.setlowerdigits("O")
        self.sethigherdigits("A")
        self.setlowerinfinity("I")
        self.sethigherinfinity("E")
        self.setloweroctave("U")
        self.sethigheroctave("")
    
class LaegnaBase4(LaegnaDigitSet):
    def __init__(self):
        self.setlowerdigits("IO")
        self.sethigherdigits("AE")
        self.setlowerinfinity("QP")
        self.sethigherinfinity("OR")
        self.setloweroctave("U")
        self.sethigheroctave("")

class LaegnaBase8(LaegnaDigitSet):
    def __init__(self):
        self.setlowerdigits("12")
        self.sethigherdigits("34")
        self.setlowerinfinity("56")
        self.sethigherinfinity("78")
        self.setloweroctave("0")
        self.sethigheroctave("9")

class LaegnaBase16(LaegnaDigitSet):
    def __init__(self):
        self.setlowerdigits(["IJ", "OP"])
        self.sethigherdigits(["AB", "EF"])
        self.setlowerdigits(["KL", "QR"])
        self.sethigherdigits(["CD", "GH"])
        self.setloweroctave("UV")
        self.sethigheroctave("W")

