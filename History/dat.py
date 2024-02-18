

class DataDen():
    def __init__(self, den = "U"):
        self.den = den

# This is the container of one bit or array of ones bits (dens)
# They are registered in Dimension Map
class DataSource:
    def __init__(self, dimensionmap):
        self.dimensionmap = dimensionmap
        self.dens = {}

    def addDen(self, index):
        self.dens[index] = DataDen()

