# = Document Abstraction Class

# This abstracts three types of Documents:
# - __Folders__: Structural Documents.
# - __Python Scripts__: Executable Documents.
# - __Markdown Files__: Text Documents.

# We might add Document Types: Json, HTML,
# CSS and others, giving each a magic ability
# to form Markdown Structures for easy readability.

# Each type has some unique properties:
# - __Python Documents define API's__ for easy
#   access. Class and definition headers
#   should appear along with code blocks.
#
#   We should visualize this process:
#   - Depending on file type, a Standard Lmw
#     APIs should generate forms to test
#     input, other APIs should generate
#     API structures.
#
# - __Filestructure Documents define
#   Attachments__: with filestructures,
#   attachments are easy and require no
#   special work.
#
# - __Markdown Documents define easy-to-edit
#   interfaces__: we can allow easy creation
#   of Text Documents, but with power of
#   Markdown, we can follow the standard and
#   it's extensions to HTML, LaTeX for Math,
#   and achieve Standard For Structured
#   Information.

# The code is meant to float around, and
# while it has _practical_ applications, it
# also has _generic_ ideals, which are kept
# intact from specialized or particular code,
# where it would contain essentials and be
# able to act as a Template.

# Ideally, an AI would become _really free_
# in implementing systems with similar
# functionality and creating modifications
# to _this type of systems_. Laegna Math is
# not a single project, but an attempt to
# introduce generics to implementation: this
# also means, if you are able to implement
# a concept properly in other language, even
# if it's a simple Laegna concept, you are
# welcome to contain it here.

# Find UserDict.py to understand the internals of emulated dictionary.

# Parent class, which contains blocks and documents.
class LaeBlock:

class LaeMarkdown(LaeBlock):

class LaeDocument(LaeBlock):
    def __init__(self):
        pass

    def __call__(self, *args, **kwds):
        for a in range(0, 8):
            yield a

    def __len__(self): return len(self.data)
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)
    def __setitem__(self, key, item): self.data[key] = item
    def __delitem__(self, key): del self.data[key]
