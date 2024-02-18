from testconf import *

# R octaves:
# 0: OctI A=1, AA=2; Additive: each digit is added / zero (Octave 0)
# 1: OctO Classical system with given base / finite (Octave 1)
# 2: OctA Octave base of 2 / infinite (Octave 2)
# 3: OctE Octave base of E / exponential (Octave 3)
class ROctave:
    def __init__(self, roctave = 1, verbose = False, test = False):
        loghead("Initializing ROctave, setting roctave to " + str(roctave) + " by default.")
        logsubhead("! R octave 1 is number system with approximately classical positioning.")
        self.setRoctave(roctave)

    def setRoctave(self, roctave):
        log("- DigitBase: setting roctave to " + str(roctave) + ".")
        self.base = roctave

    def getRoctave(self):
        log("- DigitBase: returning base: " + str(self.roctave) + ".")
        return self.base
    
    def getRoctavePos(self):
        # Do the position calculation
        roctavePos = 0
        log("- DigitBase: returning base dimension: " + str(roctavePos) + ".")
        return roctavePos

    def __str__(self):
        return "base-" + str(self.getBaseDim())

    def test(self):
        for testBase in range(0, 3):
            self.setBase(testBase)
            self.getBase()
            self.getBaseDim()
            log("User literal: " + str(self))

class TOctave(ROctave):
    pass

testhead("= Initializing R Octaves. =")
testsubhead("_running tests (only output is generated for manual review)_")
test(ROctave)
testfoot("Finished testing")
