# Position numbers, this means basically mapping of a number system with properties of A.

import random

# Since number mappings are highly intuitive, let's use a base class each time: base class
# is written before number type. Only higher-order numbers can abstract out this base class
# and rather reflect one, integral number system of Laegna Math - here, our logic and vision
# is not enough to understand this.

# List of indexes to baseName and baseEnum
randomize = [2, 4, 8, 10]

baseEnum = {}
baseName = {}

baseName[2] = "Den"
baseEnum[2] = "OA"
baseName[4] = "Ten"
baseEnum[4] = "IOAE"
baseName[8] = "Dec18"
baseEnum[8] = "12345678"
baseName[10] = "Dec09"
baseEnum[10] = "0123456789"

# This tries to mock you that it's basic Laegna Number generator: it gives you things, which would look like T-Laegna Numbers, not having their R-Laegna XYZ
# counterparts at all.
class LaegnaNumberMocker:
    def __init__(self):
        print("# Laegna Number Generator")

class PositionNumbers:
    baseClass = "Triv"

    # It's now Laegna python - using I instead of self
    def __init__(I):
        # Initialize with a random index
        i = random.choice(randomize)
    
    def __str__(I):
        return self.name()