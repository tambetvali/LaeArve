# Verify that we can have own own defined objects in Anytree.

import anytree

# Any class.
class X():
    def __init__(self):
        pass

    # Is our class still around?
    def __str__(self):
        return "I am here"

a = X()

x = anytree.Node("test", link=a)

print(x.link)

print(x)