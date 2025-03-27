from fractions import Fraction

def repeating_decimal_to_float(repeating_part: str) -> float:
    """
    Converts a repeating decimal sequence into a floating-point number.
    
    Special handling:
    - If 'A' is present in the input, it represents a broken base system and results in infinity.
    - Otherwise, the function calculates the correct repeating decimal value.

    :param repeating_part: A string representing the repeating digits (e.g., '3' for 0.(3), '142857' for 0.(142857))
    :return: The corresponding floating-point value, or infinity if 'A' is present.
    """
    # If 'A' is present, return infinity to represent the broken base case
    if 'A' in repeating_part:
        return float('inf')

    # Convert to integer value
    int_value = int(repeating_part)
    length = len(repeating_part)

    # Compute the fraction
    fraction = Fraction(int_value, int('9' * length))

    # Convert to float
    return float(fraction)

def repeating_decimal_to_float_frequential(repeating_part: str) -> tuple:
    """
    Converts a repeating decimal sequence into a floating-point number using a dual representation system:
    
    - Numbers 0-9 are calculated as fractions of themselves.
    - A secondary number is introduced where 'A' is treated as 1 in its respective decimal position.
    - If 'A' is present, it results in infinity to represent the broken base case.

    :param repeating_part: A string representing the repeating digits (e.g., '3' for 0.(3), '142857' for 0.(142857))
    :return: A tuple with both primary and secondary floating-point values, or infinity if 'A' is present.
    """
    
    # Primary number calculation (normal fraction)
    int_value = int(repeating_part.replace('A', '0'))  # Replace 'A' with '0'
    length = len(repeating_part)
    fraction = Fraction(int_value, int('9' * length))
    
    # Secondary number calculation (frequential representation)
    secondary_value = sum(1 if ch == 'A' else 0 for ch in repeating_part)
    secondary_fraction = Fraction(secondary_value, int('9' * length))
    
    # Return both calculated values as a tuple
    return float(fraction), float(secondary_fraction)

# Example usage
examples = ["3", "6", "9", "142857", "A", "0A"]

print("Normally, digit 10 where there are only 9 digits in base-10 is considered \"infinity\"")
print("In our example, we add frequential support for digit 'A' as digit 1 in higher frequency, having thus modified the space into exponential space")

for ex in examples:
    print(f"Repeating sequence: 0.({ex}), Result: {repeating_decimal_to_float(ex)}")
    primary, secondary = repeating_decimal_to_float_frequential(ex)
    if secondary:
        print(f"Repeating sequence: 0.({ex}), Result: R{secondary} T{primary}, where in Laegna system, space separates the R and T, where R is now")
        print("more than zero, where the output would be otherwise infinite.")
    else:
        print("For this number, Laegna answer is the same.")