# This is not a code file for the project, but rather the test and implementation of digits.md,
# the documentation. Rather than aiming the implementation, it implements the trivia of
# basic algorithms, but not for example all the class structure to do something already useful
# with them.

# Laegna basic class:
# 1. It has the initial implementation to support basic numeric values, which are used by
#    "assembler" phase of the initialization (in my Laegna Coding Terms, where it means to
#    implement basic numbers). It's convinient way to get the values of I, O, A, E.
# 2. Once the system is ready and loaded, it will switch to support more numbers. Later-coming
#    initializations of the class use actual Laegna numbers, not the basic "mock" to support
#    initialization, where for example ponegative values are needed. It will support the basic
#    values, some 2-3 letter values, and it would be able to convert to other Laegna formats,
#    also the "type" will start to work in addition to laevalue to support custom types.
#    For implementations, once it has advanced, it does not matter to have primitive type - the
#    more basic values, the "assembler", might fall to cycle if theirs would also be replaced.
class L:
    def __init__(self, laevalue):
        self.implementation = Limplementation
        self.instance = self.implementation(laevalue)

    def getIndex(self):
        return self.instance.getIndex()

    def getValue(self):
        return self.instance.getValue()

    def getString(self):
        return self.instance.getString()

    def __eq__(self, __value):
        return self.instance.__eq__(__value)

    def __str__(self):
        return str(self.instance)

class Lprimitives(L):
    ponegation = {"Negotion": "I", "Negation": "O", "Position": "A", "Posetion": "E",
                  "Uneton": "U", "Neglection": "V"}
    shortindex = {"I": "I", "O": "O", "A": "A", "E": "E", "U": "U", "V": "V"}
    short_ponegation = {"No": "I", "Na": "O", "To": "A", "Po": "E",
                  "Un": "U", "Neg": "V"}
    logic = {"Yes": "A", "No": "I"}
    numbers = {-2: "I", -1: "O", 0: "U", 1: "A", 2: "E", 4: "V"}
    laenumbers = {"1": "i", "2": "o", "3": "a", "4": "e", "5": "I", "6": "O", "7": "A", "8": "E",
                  "0": "u", "9": "V"}

    def __init__(self, laevalue):
        if laevalue in self.ponegation:
            self.type = "ponegation"
            self.baselae = self.ponegation[laevalue]
        if laevalue in self.shortindex:
            self.type = "ponegation"
            self.baselae = self.shortindex[laevalue]
        if laevalue in self.short_ponegation:
            self.type = "short_ponegation"
            self.baselae = self.short_ponegation[laevalue]
        if laevalue in self.logic:
            self.type = "logic"
            self.baselae = self.logic[laevalue]
        if laevalue in self.numbers:
            self.type = "numbers"
            self.baselae = self.numbers[laevalue]
        if laevalue in self.laenumbers:
            self.type = "laenumbers"
            self.baselae = self.laenumbers[laevalue]
        if not self.baselae: Exception("I do not know the number.")
        self.value = laevalue

    def getIndex(self):
        return self.value

    def getValue(self):
        return self.baselae

    def getString(self):
        return self.value + " (" + self.baselae + ")"

    def __eq__(self, __value: object) -> bool:
        return self.getValue() == __value.getValue()

    def __str__(self):
        return self.baselae

Limplementation = Lprimitives

print(str(L("Negotion")))
print(str(L("Negation")))
print(str(L("I")))
print(str(L("8")))
print(str(L("4")))
print(str(L("Posetion") == L("I")))
