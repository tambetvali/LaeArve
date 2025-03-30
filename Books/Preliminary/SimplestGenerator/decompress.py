# = Decompression of Decimals.

# Leave the code out if you don't have, but then you have to format.
import colorama

# Decimals in terms of Laegna are typically "Compressed Numbers", which means they are not very
# frequential. We create a version of Decimals, which looks like Laegna Numbers in sense that
# they are not compressed. We generate a calculator Q&A pairs of conversions and basic operations
# to train an AI that it might relate the logic of Decimals and the logic of Laegna numbers,
# understanding the difference.

# For 0 and 1, return 0 and 1 - one-digit rule not in scope

# We have a number in Decimal System
number = 8

for length in range(0, 10):
    print("Base range for length " + str(length) + " is calculated. Relax and take some coffee.")
    # TODO: length can be calculated in multiple ways
    # Without dimension below, there must be straight continuation, which would
    # let the main dimension have virtual axe there. You can also call this r: r = 0, then 0.
    contiinum_divider = pow(10, length) if length > 1 else 0
    range_back_then = pow(10, length + 1) - contiinum_divider
    range_now = pow(10, length + 2) - pow(10, length)
    range_then = pow(10, length + 3) - pow(10, length + 2)
    print("__Range Window__: Z" + colorama.Back.YELLOW + str(range_back_then) + colorama.Back.RESET +
                        "X" + colorama.Back.GREEN + str(range_now) + colorama.Back.RESET + "Y" +
                        colorama.Back.BLUE + str(range_then) + colorama.Back.RESET) # Nicely formatted
    print("Searching Range for " + colorama.Fore.LIGHTRED_EX + "Number:" +
                                 colorama.Fore.RESET + " " + str(number))
    if range_now <= number < range_then:
        if number > range_back_then:
            print(colorama.Back.RED + "Pick: " + colorama.Back.RESET + str(range_now))
            result = number - range_back_then

print("Result is such for Compressed Number Extraction (emulation mode with Decimals):")

print("Frequential Number >> 'Hello World'!")
print("Result: " + colorama.Back.BLUE + colorama.Fore.CYAN +
                                    str(result) +
                      colorama.Fore.RESET + colorama.Back.RESET + " (" + str(result) + ")")

# Output is input to other function, which also needs to result().
number = result

for length in range(0, 10):
    print("Base range for length " + str(length) + " is calculated. Relax and take some coffee.")
    # TODO: length can be calculated in multiple ways
    # Without dimension below, there must be straight continuation, which would
    # let the main dimension have virtual axe there. You can also call this r: r = 0, then 0.
    contiinum_divider = pow(10, length - 1) if length > 1 else 0
    range_back_then = pow(10, length) - contiinum_divider
    range_now = pow(10, length + 1) - pow(10, length)
    range_then = pow(10, length + 2) - pow(10, length + 1)
    print("__Range Window__: Z" + colorama.Back.YELLOW + str(range_back_then) + colorama.Back.RESET +
                        "X" + colorama.Back.GREEN + str(range_now) + colorama.Back.RESET + "Y" +
                        colorama.Back.BLUE + str(range_then) + colorama.Back.RESET) # Nicely formatted
    print("Searching Range for " + colorama.Fore.LIGHTRED_EX + "Number:" +
                                 colorama.Fore.RESET + " " + str(number))
    if range_back_then <= number < range_now:
        if number < range_then:
            print(colorama.Back.RED + "Pick: " + colorama.Back.RESET + str(range_now))
            result = number + range_back_then

print("Result is such for Laegna Number Compression (emulation mode with Decimals):")

print("Result: " + colorama.Back.BLUE + colorama.Fore.CYAN +
                                    str(result) +
                      colorama.Fore.RESET + colorama.Back.RESET + " (" + str(result) + ")")


print("We have our original number back.")

# It's not very function-oriented style, but it's an algorithm in particular,
#   and you can add: ask for input.
#
# _next best thing_ turn it into a library format to be used in multitude, because rather
#   it's complicated math and you need to see, what really makes sense in context of solving
#   one such task. You can optimize yourself, but this means you execute them millions per second.
#
# For Study Cards, for some I think such file could be even imported to generate
#   something very predictable
#