from testconf import *

# Number Dimensionality:
# Byte: Each bit represents presence or absence of a dimension; the base dimension is always there
class NumberDimension:
    def __init__(self, dimensionality = 0):
        loghead("Initializing NumberDimension, setting dimensionality to " + str(dimensionality) + " by default.")
        logsubhead("! Dimensionality of 0 contains only the number digit.")
        self.setDimensionality(dimensionality)

    def test(self):
        # Checking some random dimensions, such as in dimensionality 1, dimension 1 should exist.
        # These few tests would fail in case of trivial errors, such as not doing the operation at
        # all, while more complex errors are rather about testing.
        # TODO: one can implement a more complex test.
        for dimensionality in [(0, 1, False), (1, 1, True), (2, 2, True)]:
            self.setDimensionality(dimensionality)
            self.getBase()
            self.getBaseDim()
            log("User literal: " + str(self))

    def setDimensionality(self, dimensionality = 0):
        log("- NumberDimension: setting dimensionality to " + str(dimensionality) + ".")
        self.dimensionality = dimensionality

    def getDimensionality(self, dimensionality = 0):
        log("- NumberDimension: returning dimensionality: " + str(self.dimensionality) + ".")
        return self.dimensionality
    
    def str(self):
        dimstr = "dim(+ | "
        for dimension in range(0, 7):
            true = pow(2, dimension) and self.dimensionality
            if true:
                dimstr += "+"
            else:
                dimstr += "-"
        dimstr += ")"
        return dimstr

    def hasDimension(self, dimension):
        if dimension == 0: return True
        return dimension and (1 << dimension)

testhead("= Initializing Number Dimension Tests. =")
testsubhead("  _running tests (only output is generated for manual review)_")
test(NumberDimension)
testfoot("Digit base test finished")