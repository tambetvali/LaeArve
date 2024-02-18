import math

def multser(m, divider = 1):
    print("Multiplier", m)
    for a in range(0, 10):
        print(a, m, math.floor(pow(m, a) / divider))

multser(2, 1)

print([None] * 3)