# All the MD needed by Trivial Things
# They don't need specific class, because no example is nesting another example, so we don't
# overOOP to help out with correct classes - we don't have that notion as we have it not interacting,
# so we optimize out the unused variable property, it's class, of the actual parser. Instead we give
# it a singeton instance; kind of half-singleton I don't know if ther's a word.

markdown = ""

def header(title):
    markdown += "# " + title + "\n"

