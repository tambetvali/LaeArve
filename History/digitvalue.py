

# Where dim = 1:
# U, 0: Digit is U, or contained in a group, which is U.
# O, 1: Digit is O, or contained in a group, which is O
# A, 2: Digit is A, or contained in a group, which is A
# For example, if the atom is in base power 2, UOA map to VIE, which is why Dens do not
# have V - V is just a higher-frequency U, like IE are higher frequency OA, and thus it's
# mapped with the same logic, by having more powerful or higher-order Dens forming actual Tens.
# Where dim = 2:
# U, O, A are allowed.
# I, 3: Digit is I.
# E, 4: Digit is E.
# V, 5: Digit is V.
# Retced, in Estonian, sounds like "retked", which means travellings; in Laegna, it can be used to
#   separate between things, which happen with ultimate R.
# Dimension 1: It contains UOA, which is "S".
# Dimension 2: It adds IEV, which is "T".
# Dimension 3: For 8-based values, the "R" refers that first group is the velocity group in local space,
#   the second group is the acceleration group. For complex part of a number alone, it's one or another,
#   but 0 is used as the local component size is rather T than R in regards to 18 infinity.
# TODO: you can add some error handling
from typing import Any


class DigitValueAtom:
    def __init__(self, value = "A", dim = 1, retced = 0):
        self.setValue(value, dim, retced)
    
    def setValue(self, value = "A", dim = 1, retced = 0):
        if value == "U": value = 0
        if value == "O": value = 1
        if value == "A": value = 2
        if dim != 1: # For one-dimensional number won't pass this point
            if value == "I": value = 3
            if value == "E": value = 4
            if value == "V": value = 5
        self.value = value
    
    def getValue(self, signed = False):
        if signed:
            if self.value == "O": return -1
            if self.value == "A": return 1
            if self.value == "U": return 0
        if not signed:
            if self.value == "U": return 0
            if self.value == "O": return 1
            if self.value == "A": return 2
        if self.dim == 1: return # For one-dimensional number won't pass this point
        if signed:
            if self.value == "I": return -2
            if self.value == "E": return 2
            # In Laegna language, if 0 is between -1 and 1, symmetrically 4 would be exbetween -2 and 2
            if self.value == "V": return 4
        if not signed:
            if self.value == "I": return 1
            if self.value == "E": return 2
            if self.value == "V": return 5

# One of I, O, A, E
baseDigitI = DigitValueAtom("I")
baseDigitO = DigitValueAtom("O")
baseDigitA = DigitValueAtom("A")
baseDigitE = DigitValueAtom("E")

def getBaseDigit(digit = "A"):
    global baseDigitI, baseDigitO, baseDigitA, baseDigitE
    if digit == "I": return baseDigitI
    if digit == "O": return baseDigitO
    if digit == "A": return baseDigitA
    if digit == "E": return baseDigitE

# Decompose digits into Atoms
class DigitValueAtomic:
    def __init__(self, digit = 0, , size = 1):
        pass

# This represents:
# - A single digit
# - A single digit component of digit on several positions, such as multiline or RT numbers
class DigitValue:
    def __init__(self, letter = getBaseDigit(), accents = [None] * 8, # letter
                 color = None, boldItalic = None, caps = getBaseDigit()): # letter's style
        self.setDigitValue(letter, accents, color, boldItalic, caps)

    def setDigitValue(self, letter = getBaseDigit(), accents = [None] * 8, # letter
                            color = None, boldItalic = None, caps = getBaseDigit()): # letter's style
        self.letter = letter
        self.accents = accents
        self.color = color
        self.boldItalic = boldItalic
        self.caps = caps
