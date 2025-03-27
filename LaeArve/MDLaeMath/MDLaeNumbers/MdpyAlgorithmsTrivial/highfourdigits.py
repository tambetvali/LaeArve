
I = "I"
O = "O"
A = "A"
E = "E"

Ten = [I, O, A, E]
Den = [O, A]

# Standard ponegative R and T; many R and T mappings exist.
for i in range(len(Ten)):
    # "Get 'column'" of Ten-value matrix
    R = i % 2

    # "Get 'row'" of Ten-value matrix
    T = int(i / 2)

    print(i, T, R)

    print("For digit `" + str(i) + "` (`" + Ten[i] + "`), R=`" + Den[R] + "` and T=`" + Den[T] + "`")

    print("`Dene(R=" + Den[R] + ", T=" + Den[T] + ") = Ten(" + Ten[i] + ")`")

    print("Checking R and T for low-frequency Ten to understand, was it an illusion:")
    if R == T:
        print("R=T: This is a very Realistic Ten!")
    else:
        print("R!=T: This is Maya, it's a big illusion you microphone abuser!")

