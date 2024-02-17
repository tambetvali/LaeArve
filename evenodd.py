import colorama
from testconf import *

# Parity of the number or digit, isodd:
# True: The number has no zeroes or unknowns
# False: The number has zeroes or unknowns
# Parity of the parity itself, isEven:
# True: Space or another shape like U or X or _ could be used to lack the digit
# False: Every digit must exist
# In case of lacking any parity, you round to the closest number, as if V was resolved.
# For negative parities, use isfair and isFair where true means the number matters in calculations,
# which are then considered fair:
# V, the weak negative parities means that the actual digit value is it's linear position in the content.
# W, the strong negative parity means that it's to be calculated in infinity.
# Additionally, we set whether we can have limit values with exclamation mark before and after number:
# limits = "none" if we cannot do this.
# limits = "after" if the exclamation mark goes after the number.
# limits = "bound" is the exclamation mark goes after or before the number.
# If used in context of sentences, the limit would find boundaries of the first or last word.
# Numbers with limits can be local or unable to grow in number systems.
# In our initial version we do not support limits. TODO: remove this message once they are implemented.
# We might consider to call them "boundaries", where the number might be bounded. We run into
# hard math because correctly comparing and utilizing such numbers means we need to calculate differences
# of numbers, such as 2 * 2 giving 4, but inside the 4 there is still some difference of being 2 * 2 not
# 1 * 4 - the differences of boundary values are the same, they exist only logically not numerically,
# where Logecs can be mapped to numbers anyway, but we get false answers if we consider them equal or
# inherently unknown; thus we have to track the logic of them to properly calculate, and "prove" which
# ones are meant.

# Ô-ôômega, which we do not contain here as it's not part of the _strict_ number types (ones, which do
# not directly contain exceptions coming from higher math, linguistic structures or poetry); instead of
# computing, we rather _reason_ about those: we will not implement it in numeric primitives handled by
# assembler, programming language or strict syntax, but in derived number systems, where we can already
# use advanced math and proofs based on the low-level system, which is rather mappable to linear
# coordinates. If you don't known a number at all, you don't map this case trivially to linear
# coordinates, but each is a special case; for example if you don't know, whether nature has awareness
# or is made of matter, the system to make implications of such unknown is not based solely on basic
# calculations with numbers, whereas ô and ô-ôômega, local and global version of this, are meant to
# do these calculations.
class Parity:
    def __init__(self, isodd = True, isOdd = True, isfair = True, isFair = True, limits = "none", verbose = False, test = False):
        loghead("Initializing Parity, " + colorama.Fore.GREEN + "setting" + colorama.Fore.BLUE + " isodd to " + str(isodd) + " and isOdd to " + str(isOdd) + ",")
        logsubhead("           and also " + colorama.Fore.GREEN + "setting" + colorama.Fore.RESET + " isfair to " + str(isfair) + " and isFair to " + str(isFair) + " by default.")
        logsubhead("                 By " + colorama.Fore.GREEN + "default" + colorama.Fore.RESET + ": the number or number system does not support limits, it's set to \"none\".")
        logsubhead("! Completely odd, but fair and limitless number does not have any notions of Zero, which is the default.")
        self.setParity(isodd, isOdd, isfair, isFair, limits)

    # We will hardly use this, but it makes testing more convienient
    def setParityFast(self, bound = False):
        self.isodd = not bound
        self.isOdd = not bound
        self.isfair = not bound
        self.isFair = not bound
        self.limits = "bound" if bound else "none"

    def setParity(self, isodd = True, isOdd = True, isfair = True, isFair = True, limits = "none"):
        self.isodd = isodd
        self.isOdd = isOdd
        self.isfair = isfair
        self.isFair = isFair
        self.limits = limits
        log("- DigitBase: setting base to " + str(self) + ".")

    def getParity(self):
        log("- DigitBase: returning base: " + str(self.base) + ".")
        return self.base
    
    def __str__(self):
        if self.isodd == True and self.isOdd == True and self.isfair == True and self.isFair == True and self.limits == "none":
            return "boundless-number"
        if self.isodd == False and self.isOdd == False and self.isfair == False and self.isFair == False and self.limits == "bound":
            return "bounded-number"
        boundstr = "Bounds("
        boundstr += "odd" if self.isodd else "even"
        boundstr += ", " if boundstr else ""
        boundstr += "Odd" if self.isodd else "Even"
        boundstr += ", " if boundstr else ""
        boundstr += "fair" if self.isfair else "ethical"
        boundstr += ", " if boundstr else ""
        boundstr += "Fair" if self.isodd else "Ethical"
        if self.limits == "none": boundstr += "open"
        if self.limits == "after": boundstr += "inwards-bound"
        if self.limits == "bound": boundstr += "bound"
        boundstr += ")"

        return boundstr

    def test(self):
        # TODO: you can test specifics
        self.setParityFast(False)
        log("User literal after setting it to bound: " + str(self))
        self.setParityFast(True)
        log("User literal after setting it to limitless: " + str(self))

start_tests()
testhead("= Initializing Parity. =")
testsubhead("  _running tests (only output is generated for manual review)_")
test(Parity)
testfoot("Parity test finished.")
stop_tests()