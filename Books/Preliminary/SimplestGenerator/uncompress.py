# # Decompressing Negative Numbers

import colorama

number = -1429

for length in range(0, 10):
    print("Base range for length " + str(length) + " is calculated. Relax and take some coffee.")
    # TODO: length can be calculated in multiple ways
    # Without dimension below, there must be straight continuation, which would
    # let the main dimension have virtual axe there. You can also call this r: r = 0, then 0.
    contiinum_divider = pow(10, length - 1) if length > 1 else 0
    range_then = pow(10, length) - contiinum_divider
    range_now = pow(10, length + 1) - pow(10, length)
    range_back_then = pow(10, length + 2) - pow(10, length + 1)
    print("__Range Window__: Z" + colorama.Back.YELLOW + str(-range_back_then) + colorama.Back.RESET +
                        "X" + colorama.Back.GREEN + str(-range_now) + colorama.Back.RESET + "Y" +
                        colorama.Back.BLUE + str(-range_then) + colorama.Back.RESET) # Nicely formatted
    print("Searching Range for " + colorama.Fore.LIGHTRED_EX + "Number:" +
                                 colorama.Fore.RESET + " " + str(number))
    print(range_back_then - number, range_back_then, range_now, range_then)
    if -range_back_then <= number < -range_now:
        print(colorama.Back.RED + "Pick: " + colorama.Back.RESET + str(range_now))
        result = range_now - number

print("Result is such for Compressed Number Extraction (emulation mode with Decimals):")

print("Frequential Number >> 'Hello World'!")
print("Result: -" + colorama.Back.BLUE + colorama.Fore.CYAN +
                                    str(result) +
                      colorama.Fore.RESET + colorama.Back.RESET + " (-" + str(result) + ")")

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
