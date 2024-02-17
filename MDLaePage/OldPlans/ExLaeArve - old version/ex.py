import mpmath as mp

# Set the precision to 50 decimal places
#mp.mp.dps(100)

# Create a complex number with real part 1 and imaginary part 2
#x = mp.mp.complex(1, 2)
#print(x)

# Generate a random number between 0 and 100 (inclusive)
x = mp.rand()
print(x)

# Move a floating-point number up one exponent level
x = mp.mp.exp(1) * 100
print(x)

# Move a floating-point number down one exponent level
x = mp.mp.log(100) / mp.mp.log(10)
print(x)


# Format a number as scientific notation
x = mp.format.scientific(100)
print(x)

# Format a number as engineering notation
x = mp.format.engineering(100)
print(x)

# Get the exponent of a number
x = mp.format.exponent(100)
print(x)

