# Numbers in Laegna System

Aim: to create classes to do normal math operations, initially with basic, but strict Laegna numbers, with intent of giving examples to humans and letting people to train their AI's to understand the combinatorics background of mine.

## Laegna basic class L:

Use cases:
- In "History" folder, which is meant to understand, what this project represents, or where one can find basic classes to define something about numbers, or to use my updated code logic in some other way, basically to study from a mistake - I like to make one or two mistakes in initial phases of projects, to get some compiler feedback and to see, where I get stuck with simplicity and elegance of the implementation process; we need anxiety for elegant solutions.
- The use case: I implemented several times, logic to simply contain some basic types in self-explanatory one-digit integers, and while I don't know what one is going to do with digits in this class, and what they would mean, it's a standard index header, where for Laegna Numbers and other Laegna code you can use it to represent, at least, the four basic Truth Values in standard way, where you don't consider whether it's upper or lower case, for example. IT allows to update itself, not by committing new version to Git, but by your program or AI having staged loader / staged loading process, where more is known about the numbers later in the process, but you keep the older objects using compatible objects they can understand and implement without additional effort and self-referencial cycles, where new objects already _interpret_ the aspects they did not know.

To have constants I, O, A, E to consistently use in binary contexts, we implement this. It allows to create index values, which remind of some basic characters and letters of Laegna, and while each has only the most basic set of characters and operations, you can for example have ponegate such as "Posetion" and know it's a standard way to write it and to compare, even to "I".
- It can be automatically updated to another class, which has another set of Ten-based indexes with named labels, and which is able to accept more values programmatically. We do not go to self-referential condition of somehow relying, or on this in advance, and replacing the actual numbers, where it's ready (we could keep the string identifier and switch class without actually reloading the object); rather, to keep linear dependencies, the old objects remain with their initial implementation, while the new objects must be able to compare with the basic letters.
- If comparison of some object is not based on it's one-letter, simplified operation, I think it also needs precision, such as L("48", precision=True), or you might use small letter "l" for this.
- Different contexts could load different values, implementing always the basic class, but having also their own implementation, which knows their precision and settings; it needs to be able to _compare_ with the base class, based on that indexes are converted to IE range, U or V.

1. It has the initial implementation to support basic numeric values, which are used by "assembler" phase of the initialization (in my Laegna Coding Terms, where it means to implement basic numbers). It's convinient way to get the values of I, O, A, E.
2. Once the system is ready and loaded, it will switch to support more numbers. Later-coming initializations of the class use actual Laegna numbers, not the basic "mock" to support initialization, where for example ponegative values are needed. It will support the basic values, some 2-3 letter values, and it would be able to convert to other Laegna formats, also the "type" will start to work in addition to laevalue to support custom types. For implementations, once it has advanced, it does not matter to have primitive type - the more basic values, the "assembler", might fall to cycle if theirs would also be replaced.

Notice that if you enter binary "No", the type is lost - but you get the proper return value "No (I)", because you cannot query for the type.

### Basic implementation of Class L

__Laegna basic class:__

1. It has the initial implementation to support basic numeric values, which are used by "assembler" phase of the initialization (in my Laegna Coding Terms, where it means to implement basic numbers). It's convinient way to get the values of I, O, A, E.
2. Once the system is ready and loaded, it will switch to support more numbers. Later-coming initializations of the class use actual Laegna numbers, not the basic "mock" to support initialization, where for example ponegative values are needed. It will support the basic values, some 2-3 letter values, and it would be able to convert to other Laegna formats, also the "type" will start to work in addition to laevalue to support custom types. For implementations, once it has advanced, it does not matter to have primitive type - the more basic values, the "assembler", might fall to cycle if theirs would also be replaced.

```python
class L:
    def __init__(self, laevalue):
        self.implementation = Limplementation
        self.instance = self.implementation(laevalue)

    def getIndex(self):
        return self.instance.getIndex()

    def getValue(self):
        return self.instance.getValue()

    def getString(self):
        return self.instance.getString()

    def __eq__(self, __value):
        return self.instance.__eq__(__value)

    def __str__(self):
        return str(self.instance)

class Lprimitives(L):
    ponegation = {"Negotion": "I", "Negation": "O", "Position": "A", "Posetion": "E",
                  "Uneton": "U", "Neglection": "V"}
    shortindex = {"I": "I", "O": "O", "A": "A", "E": "E", "U": "U", "V": "V"}
    short_ponegation = {"No": "I", "Na": "O", "To": "A", "Po": "E",
                  "Un": "U", "Neg": "V"}
    logic = {"Yes": "A", "No": "I"}
    numbers = {-2: "I", -1: "O", 0: "U", 1: "A", 2: "E", 4: "V"}
    laenumbers = {"1": "i", "2": "o", "3": "a", "4": "e", "5": "I", "6": "O", "7": "A", "8": "E",
                  "0": "u", "9": "V"}

    def __init__(self, laevalue):
        if laevalue in self.ponegation:
            self.type = "ponegation"
            self.baselae = self.ponegation[laevalue]
        if laevalue in self.shortindex:
            self.type = "ponegation"
            self.baselae = self.shortindex[laevalue]
        if laevalue in self.short_ponegation:
            self.type = "short_ponegation"
            self.baselae = self.short_ponegation[laevalue]
        if laevalue in self.logic:
            self.type = "logic"
            self.baselae = self.logic[laevalue]
        if laevalue in self.numbers:
            self.type = "numbers"
            self.baselae = self.numbers[laevalue]
        if laevalue in self.laenumbers:
            self.type = "laenumbers"
            self.baselae = self.laenumbers[laevalue]
        if not self.baselae: Exception("I do not know the number.")
        self.value = laevalue

    def getIndex(self):
        return self.value

    def getValue(self):
        return self.baselae

    def getString(self):
        return self.value + " (" + self.baselae + ")"

    def __eq__(self, __value: object) -> bool:
        return self.getValue() == __value.getValue()

    def __str__(self):
        return self.baselae

Limplementation = Lprimitives
```

## Compressed <=> Balanced representation of numbers, conversion and containment class

Background: In the first version, we are going to implement the numbers to meet the minimal requirements. Over time, we aim to get into multitude of number representation classes, which would allow to use different aspects well; we are also trying to integrate them into more general number theory, which would not necessarily conclude that they are different types of numbers, but it would be more aware of how they relate to operations and their aims, and how the same _quantities_ and _qualities_ in number definition create those approaches of number use - much like having indexes of objects and structures, we would not have any property of this external reality attributed by number theory a priory; rather we can assign very different numbers to same, or same numbers to different format. Each number system tries to compensate those effects and to generalize, what it does with numbers - for example, in decimal system it's easy to denote positive numbers with negative, and negative numbers with positive, regarding to a variable, which is simply negation of the more relevant and theoretically symmetric variable we are supposed to use; such as, while it's not direct requirement, energy is not a negative measure, typically. You have to learn the Laegna paradigm - how it rather uses the simple metaphors of structures of infinity, than flat appearances to describe the numbers; indeed, for human sake it's often just "big number" or "small number", and we use discrete continuous systems for that - we map continuous scales to discrete numbers in a way that properties and relations are kept, while the correlations in the number are not very fixed or static, which would rather resemble topology and use some rules of this science; it's not solely topological as to be topological system, we would need to attribute the shape symmetries as topological property: when an angle of a line is not necessarily topological value, the fact that it goes upwards, and not too much, has qualities rather than quantities or particulars; the discrete set is assigned in a way that solid borders are kept, and for example number is not dividing quantities, which do not matter in our regards.



```python
Class BalancedNumber:
  

```