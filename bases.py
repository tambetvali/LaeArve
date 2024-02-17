from testconf import *

# Digit Bases:
# 0: Base 1
# 1: Base 2
# 2: Base 4
# 3: Base 8
class DigitBase:
    def __init__(self, base = 1, verbose = False, test = False):
        loghead("Initializing DigitBase, setting base to " + str(base) + " by default.")
        logsubhead("! Digit Base 1 is Base-2 Number System Dialect")
        self.setBase(base)
    
    def setBase(self, base):
        log("- DigitBase: setting base to " + str(base) + ".")
        self.base = base

    def getBase(self):
        log("- DigitBase: returning base: " + str(self.base) + ".")
        return self.base
    
    def getBaseDim(self):
        baseDim = pow(2, self.base)
        log("- DigitBase: returning base dimension: " + str(baseDim) + ".")
        return baseDim

    def __str__(self):
        return "base-" + str(self.getBaseDim())

    def test(self):
        for testBase in range(0, 3):
            self.setBase(0)
            self.getBase()
            self.getBaseDim()
            log("User literal: " + str(self))

testhead("= Initializing Bases. =")
testsubhead("  _running tests (only output is generated for manual review)_")
test(DigitBase)
testfoot("Digit base test finished.")