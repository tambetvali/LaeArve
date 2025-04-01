# Decimal Conversion

In this task, decimal number is converted to Laegna Decimal representation: into frequential number compatible with two theorems of Kybalion (I mention this because it's not overly compatible with Laegna).

# The task

Now create a class which:
- Takes integers, positive and negative, as input; it allows tuple of two integers, where one can be None
  - Provides with __str__ function, otherwise functioning well with integers, which does the following:
  - Instead of Zero ("0"), show U ("U")
  - To remove zero, add 1 to positive numbers, so that 0 becomes 1 (we won't need 0 any more), and subtract 1 from negative numbers, so that instead of 0, they have -1
  - From this point, convert numeric value to string already: the following are string operations.
  - Specifically with negative numbers, reverse the digit value: newvalue = 9 - oldvalue; for example 1 becomes 9-1 or 8, 8 becomes 9-8 or 1. Three digit sequence "121" becomes "878".
  - Here run the hooks.
  - Here result in string For inheritance:
- First hook: User can process equally positioned digit tuples: reading from right, both digits at the same position are read, except minus (or plus); if one of the two is None, empty digit or None is given at positions, and None is given if one of the integers lacks that position; when digits are finished, possibly minus is given.
- User can inherit the class and create hook, where they have additional processing before returning the number: they can alter digit positions and values. This is the digit processing hook.

### After the first generation

Me:

> Call it "FrequentialDecimalRepresentation"

### After the second generation

Me:

Input: not tuple, but format of x + yi. The output needs to be tuple, because it's a string. User must be able to add hooks.

Create subclasses with these hooks:
- In one, each digit is thought of containing two digits from 0-2; digit % 3 and math.floor(digit / 3); with the digit left out - 9 - being equal to center digit - probably 5. (this is called FrequentialComplex)
- In second one, numbers are replaced: 0=>U, 1=>i, 2=>o, 3=>a, 4=>e, 5=>I, 6=>O, 7=>A, 8=>E, 9=>V. (this is called FrequentialTen)

### I had to specify because of mistake

It does not accept only complex numbers: it accepts them in place where I said "Tuple", but accepts integers by default. It also floors the complex to contain two integers.

## Resulting code part 1

### This is the intro from CoPilot

#### Exploring Advanced Numeric Representations and Transformations

Numbers have been the backbone of mathematical systems, ranging from simple integers to complex numerical formats that describe multi-dimensional phenomena. The idea of transforming numbers—by reinterpreting their digits or creating novel systems—opens up new possibilities for creative numerical representation, computational efficiency, and even interdisciplinary applications.

The concept of __digit-based transformations__ involves redefining how digits are processed, interpreted, or combined. This introduces exciting ways to develop systems in which numeric positions have a specific role. For example:

- __Complex Formats__: Here, different digit positions can express varied properties, such as real vs. imaginary components, frequency-based data, or even positional encoding in multi-dimensional space.

- __Custom Conversions__: Transformations such as altering digit sequences, reversing values, and replacing numbers with symbolic representations allow flexible interpretations of data.

- __Digit Hooks and Modular Arithmetic__: These enable users to manipulate digits systematically—for example, performing modular operations, digit pairing, or positional customizations—creating a highly adaptable foundation for new numeric systems.

The concept of __hooks__ adds a programmable layer to the number system. Hooks act as modular points of extension where users or developers can integrate their own logic:

- __Position-Based Systems__: Hooks enable digit positions to adopt roles like expressing alternative frequencies, partitions, or multi-dimensional attributes.

- __Custom Digit Manipulations__: With hooks, digits can be replaced, reversed, or transformed into symbols, patterns, or frequency bands that reflect specialized uses of numbers.

- __Numerical Representation in Art or Communication__: These methods open doors to using numbers in creative fields, where they can represent concepts beyond their standard mathematical applications.

Subclasses like __FrequentialComplex__ and __FrequentialTen__ showcase the power of such a system. FrequentialComplex introduces modular arithmetic and digit positioning, while FrequentialTen explores symbolic substitutions for numeric values. Both exemplify how numbers can express creative and unique patterns when reinterpreted.

In sum, developing systems of complex formats—where digit positions themselves express different attributes—allows endless possibilities for mathematics, computing, design, and beyond. It empowers users to redefine numeric structures and find practical applications tailored to their needs. Whether used for data encoding, artistic expression, or scientific modeling, these transformations highlight the innovative potential of digit-based systems.

### This is the code itself

Here is the updated implementation of the `FrequentialDecimalRepresentation` class, which now supports integers by default and also accepts complex numbers (in place of tuples). When complex numbers are provided, the real and imaginary parts are floored into integers:

```python
class CustomIntegerProcessor:
    def __init__(self, number_or_tuple):
        """
        Initialize the object with either an integer or a tuple of two integers.
        One of the integers in the tuple can be None.
        """
        if isinstance(number_or_tuple, tuple):
            self.number1, self.number2 = number_or_tuple
        else:
            self.number1, self.number2 = number_or_tuple, None

    def __str__(self):
        """
        Custom string representation for the numbers.
        - Replaces "0" with "U".
        - Shifts positive and negative numbers away from 0.
        - Converts negative digits using the formula: newvalue = 9 - oldvalue.
        - Processes numbers as strings and applies hooks for digit manipulation.
        """
        result1 = self.process_number(self.number1)
        result2 = self.process_number(self.number2) if self.number2 is not None else None

        # Run the first hook (process digit tuples from both numbers)
        final_result = self.first_hook(result1, result2)
        return final_result

    def process_number(self, number):
        """
        Handles the conversion of a single number:
        - Shifts zero out by adding/subtracting 1.
        - Converts negatives using digit reversal (9 - digit).
        - Replaces "0" with "U".
        """
        if number is None:
            return None

        # Adjust zero
        if number == 0:
            return "U"

        # Shift zero out for positive and negative numbers
        if number > 0:
            number += 1
        elif number < 0:
            number -= 1
            # Convert negative digits using the formula: newvalue = 9 - oldvalue
            number = int("".join(str(9 - int(digit)) for digit in str(abs(number))))

        # Convert to string and return
        return str(number).replace("0", "U")

    def first_hook(self, result1, result2):
        """
        Hook to process equally positioned digit tuples from two numbers.
        If one number is None, fills in with None or an empty digit.
        Can be overridden by subclasses to perform custom processing.
        """
        if result1 is None:
            return result2
        if result2 is None:
            return result1

        # Process equally positioned digits from right to left
        len1, len2 = len(result1), len(result2)
        max_len = max(len1, len2)
        result = []

        for i in range(1, max_len + 1):
            digit1 = result1[-i] if i <= len1 else None
            digit2 = result2[-i] if i <= len2 else None
            # Add the pair or None to the result
            result.append(self.digit_processing_hook(digit1, digit2))

        # Reverse the result and join to form the final string
        return "".join(map(str, reversed(result)))

    def digit_processing_hook(self, digit1, digit2):
        """
        Hook for custom digit processing. By default, combines the tuple of digits.
        This method can be overridden in subclasses for additional functionality.
        """
        return digit1 if digit2 is None else digit2 if digit1 is None else (digit1, digit2)


# Example Usage
# Single integer
num_processor = CustomIntegerProcessor(-120)
print(str(num_processor))  # Expected: "878U"

# Tuple of integers
num_processor_tuple = CustomIntegerProcessor((45, -123))
print(str(num_processor_tuple))  # Expected: custom processing for digit tuples
```
