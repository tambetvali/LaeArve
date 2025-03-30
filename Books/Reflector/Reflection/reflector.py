
# = NodeFolder

# This folds each node with the same name,
# each together.

# Remember this core library is not dynamo:
# it does not follow, where things are referred,
# because it's insensible about infinite cycles.

# Rather we go into infinite cycle when we
# are already _inside_ the page, so that we
# can break in some 10 levels or so, without
# breaking the Module Positioning System.

#
# Our System Knows:
# - Markdown files contain _chapters_.
# - Python code, as well, returns Markdown
#   content.
#

class NodeFolder:
    def __init__(self, name = ""):
        self.name = name

# Filename is the default _index component_ to
# be mapped into url component.
# On second level, each md file or folder can
# specify the unique name of it's family,
# where the same name links them together.
# Even files from other servers should be able
# to map together.

# index.sort.md is a sorting file, which
# contains each url component in it's right
# order on separate line.
# Headers are allowed and they don't create
# an element. Links have their own target
# and do not connect to file tree.
# If definition is not found, a broken link
# appears, so that the user or developer can
# notice / be noticed to fix this null
# reference problem.
# Each of our file types is really a subset of
# Markdown format, thus .md always follows:
# the client can access the open source content.

# Each Node - File, Directory - in the current
# Branch - chapter, directory.
# Equality is simply used to add to set,
# I have my own conception of it :)
# Elements cannot be removed, it's rebuilt
# at each check - non-permanent controller.
class FolderNodes:


class Accounter:
    # Encounters and Accounts for the Nodes and Branches.
    def __init__(self, preliminaryRootFolder = ""):
        