import numpy as np
import mpmath as mp


# Position systems, encoding for my interesting systems:
# Each position equals one = RoctU; digit has it's digit value
# Positions are linear, 1 2 3 4 = RoctI; digit is multiplier for it's position
# Positions are frequential, with A 1 2 4 8 16 and E at prev digit = RoctO; the basic system of Laegna
# Positions are square, E = 2, EE = 4, EEE = 8, EEEE = 16 = RoctA
# Positions are cubic, E = 2, EE = 4, EEE = 16, EEEE = 16 * 16 = RoctE; the lossy quadratic number
# Positions grow from 1 to 2, or to 0 downwards: E = 1; EE = 2 - 0.25; EEE = 2 - 0.25 / 4 = RoctV; the infinity-compatible number
# (you could use octave values instead, given the right octave systems - these are here what I need)

class DigitPositions:
    def __init__(self, system = "RoctU"):
        self.system = system
    
    # From smaller digit value (left) to bigger digit value (right)
    # Return the E value of that position
    def decodeposition(self, n = 0):
        if self.system == "RoctU":
            return 1
        if self.system == "RoctI":
            return n
        if self.system == "RoctA":
            return pow(2, n)
        if self.system == "RoctE":
            return pow(4, n)

def digitsequence(digits = "IOAE", length = 1):
    str = ""
    for n in range(0, length):
        str += digits[np.random.randint(1, len(digits))]
    return str

class LaeNumber:
    def __init__(self):
        self.number = 0
        self.digits = [-2, -1, 1,  2]
        self.truth  = [-2,  1, 2, -1]
    
    def generate(self, length = -1):
        if length == -1:
            length = np.random.randint(0, 100)
        self.laenum = digitsequence(length = length)

    def __str__(self) -> str:
        return self.laenum

#x = mp.mpf('789e+14')
#print(x)

print(digitsequence(length = 10))

x = LaeNumber()
x.generate()
print(x)