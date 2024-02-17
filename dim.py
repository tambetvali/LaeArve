import bases
import roctaves

# Keep a little database of dimensions for each number
class DimensionMap:
    def __init__(self):
        self.map = {}
        self.autoincrementlastid = -1
    
    def appendDimension(self, dimension):
        dim = {}
        self.autoincrementlastid += 1
        dim["dimension"] = dimension
        dim["id"] = self.autoincrementlastid
        self.map[self.autoincrementlastid] = dim
        return self.autoincrementlastid

    def getById(self, id):
        return self.map[id]

# Access the database with singleton
dimensionSingleton = DimensionMap()
