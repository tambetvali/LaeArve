from xene import *

# Dimension:
# 1: Space-separated number (2 dims of digits, 1 dim of tensor)
# 2: Space and line-feed separated number (3 dims of digits, 2 dims of a matrix)
class Den(NumberSystemDialect):
    def __init__(self, dimension = 1):
        self.numerictype = "Tenet"
