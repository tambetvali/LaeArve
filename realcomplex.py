from testconf import *

# Real, Imaginary or Complex number with Type=1 (Ten):
# 0: Real number of the Ten.
# 1: Imaginary number of the Ten.
# 2: Two-Digit Complex number of the Ten.
# 3: One-Digit Complex number of the Ten.
# R, T or RT number with Type=0 (Den)
# 0: T of the Den (value).
# 1: R of the Den (type).
# 2: Two-Digit RT of the Den.
# 3: One-Digit RT of the Den.
# R, T or RT space with Type=2 (Ren)
# 0: T of the Ren (value).
# 1: R of the Ren (type).
# 2: Two-Digit RT of the Ren.
# 3: One-Digit RT of the Ren.

# Purposes of this class:
# 1. For actual data type
# 2. For projective data type (select only one part of complex Ten or Den);
#    will behave friendly if it does not exist, throwing an Exception.

class SuperDimension:
    def __init__(self, type = 1, realcomplex = 0, verbose = False, test = False):
        loghead("Initializing SuperDimension, setting type to " + str(type) + " and realcomplex to " + str(realcomplex) + " by default.")
        logsubhead("! Type 1 with realcomplex value of 0 sets this to show real number of the Ten.")
        self.setSuperdimension(type, realcomplex)

    def setSuperdimension(self, type = 1, realcomplex = 0):
        log("DigitBase: setting superdimension to " + str(type) + " and realcomplex to " + str(realcomplex) + ".")
        self.type = type
        self.realcomplex = realcomplex

    def getSuperDimension(self):
        log("DigitBase: returning type: " + str(self.type) + " and realcomplex: " + str(self.realcomplex) + ".")
        return self.type, self.realcomplex
    
    def __str__(self):
        return "type-" + str(self.getSuperDimension()[0]) + " " + "type-" + str(self.getSuperDimension()[1])

    def test(self):
        for testType in range(1, 3):
            for testRealComplex in range(1, 4):
                self.setSuperdimension(testType, testRealComplex)
                log("Base system: " + str(self))

testhead("= Initializing R Octaves. =")
testsubhead("_running tests (only output is generated for manual review)_")
test(SuperDimension)
testfoot("Finished testing R Octaves")
