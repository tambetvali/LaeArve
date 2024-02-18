from dimenum import NumberDimension
from bases import DigitBase

# Periodic digit reader
class Periodic:
    def __init__(self, base = 2, dimensionality = 1):
        self.base = base
        self.dimensionality = dimensionality
    
    # Z is lower, x is higher dimension of a bit
    def getDigit(self, number, dimension, z, x, y):
        pass

number = 1526374859

def digit(number, z, x, y, base = 10, dimensionality = 2):
    return 