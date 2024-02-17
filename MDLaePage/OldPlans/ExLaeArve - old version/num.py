import math
import numpy as np
import mpmath as mp

base16 = ["GFEH", "CBAD", "QPOR", "KIJL"]

class Digit:
    def __init__(self, fmt):
        self.fmt = fmt
        self.x = np.random.randint(0, fmt.f)
        self.y = np.random.randint(0, fmt.f)
        if np.random.randint(1, fmt.f * 4) == 1:
            self.ux = np.random.randint(0, 2) == 1
            self.uy = np.random.randint(0, 2) == 1
        else:
            self.ux = 0
            self.uy = 0

    def __str__(self):
        # Base 2
        if self.fmt.l:
            if self.ux and self.uy: return "Ü"
            if self.ux: return "U"
            if self.uy: return "Ẅ"
        if not self.fmt.l:
            if self.ux and self.uy: return "?"
            if self.ux: return "0"
            if self.uy: return "9"
        if self.fmt.f == 2 and (self.fmt.w):
            if self.fmt.l:
                if self.x == 1: l = "A"
                if self.x == 0: l = "O"
                if self.fmt.d == True:
                    if self.y == 1: l += "A"
                    if self.y == 0: l += "O"
                return l
            if not self.fmt.l:
                if self.x == 1: l = "2"
                if self.x == 0: l = "1"
                if self.fmt.d == True:
                    if self.y == 1: l += "4"
                    if self.y == 0: l += "3"
                return l
        if self.fmt.f == 2:
            if self.fmt.l:
                if self.x == 1 and self.y == 1: return "T"
                if self.x == 0 and self.y == 1: return "S"
                if self.x == 1 and self.y == 0: return "N"
                if self.x == 0 and self.y == 0: return "M"
            if not self.fmt.l:
                if self.x == 1 and self.y == 1: return "4"
                if self.x == 0 and self.y == 1: return "3"
                if self.x == 1 and self.y == 0: return "2"
                if self.x == 0 and self.y == 0: return "1"
        if self.fmt.f == 4 and (self.fmt.w == False or self.fmt.w):
            if self.fmt.l:
                if self.x == 3: l = "E"
                if self.x == 2: l = "A"
                if self.x == 1: l = "O"
                if self.x == 0: l = "I"
                if self.fmt.d == 2:
                    if self.y == 3: l += "R"
                    if self.y == 2: l += "O"
                    if self.y == 1: l += "P"
                    if self.y == 0: l += "Q"
                return l
            if not self.fmt.l:
                if self.x == 3: l = "4"
                if self.x == 2: l = "3"
                if self.x == 1: l = "2"
                if self.x == 0: l = "1"
                if self.fmt.d == 2:
                    if self.y == 3: l += "8"
                    if self.y == 2: l += "7"
                    if self.y == 1: l += "6"
                    if self.y == 0: l += "5"
                return l
        if self.fmt.f == 4 and self.fmt.d == True:
            return base16[self.x][self.y]

        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Digital:
    def __init__(self):
        self.setf(np.random.randint(1, 3) * 2)
        self.setd(np.random.randint(1, 3))
        self.setl(np.random.randint(1, 3) == 1)
        self.setw(np.random.randint(1, 3) == 1)
        self.generate()

    # Set the frequency; for example 2 is base-2, 4 is base-4
    def setf(self, f):
        print("f: ", f)
        self.f = f
    
    # Set the dimension; 1=real and 2=complex number
    def setd(self, d):
        print("d: ", d)
        self.d = d
    
    # Switch between Laegna and Decimal representation; True if Laegna
    def setl(self, l):
        print("l: ", l)
        self.l = l
    
    # True if digit is RT double-character, false otherwise
    def setw(self, w):
        print("w: ", w)
        self.w = w

    def __str__(self):
        ex = ""
        for n in self.number:
            ex += str(n)
        return ex

    # Randomly generate a number
    def generate(self):
        length = np.random.randint(1, 101)
        self.number = []
        for a in range(0, length):
            self.number.append(Digit(self))


num = Digital()
print(str(num))
