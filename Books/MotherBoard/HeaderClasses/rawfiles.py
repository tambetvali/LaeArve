# = First Part
# Reading the Raw Directories

# == Imports
#
# Import "os" and "pathlib" for filesystem and file name access.

import os
import pathlib

# == Class RawDirectory

# Build filesystem access on raw level

# Input: the root folder to process; notice TODO: it's currently relative to my filesystem
root = "/home/tvali/LaeArve"

# It generates two iterators:
# - Folders, which iterates over each item, which creates a child node
# - Items, which includes both folders and files in current folder

# This way, it's kind of tree-iterator

# The class is also a lazy loader.

# Let's call low-lever Folders Directories, where dir reminds of direction.
class RawDirectory:
    def __init__(self, dir):
        print("Raw reading: ", dir)
        self.dir = dir
        self.contain = False
    
    def __str__(self):
        return self.dir

    def lazyContain(self):
        if self.contain:
            return
        self.contain = True

        self._nodes = {}
        self._types = {}
        self._fold = {}
        for filename in os.listdir(self.dir):
            if filename[0] == ".":
                continue
            filepath = os.path.join(self.dir, filename)
            if os.path.isfile(filepath):  # Check if it's a file
                # TODO: rather use pathlib to extract extensions?
                base_type = "file"
                base_name = pathlib.Path(filename).stem
                extension = pathlib.Path(filename).suffix
            elif os.path.isdir(filepath):
                base_type = "folder"
                base_name = filename
                extension = ""
        
            if not base_name in self._nodes:
                self._nodes[base_name] = {}
                self._types[base_name] = {}
                self._fold[base_name] = False
            
            self._nodes[base_name][extension] = filename
            self._types[base_name][extension] = base_type
            if base_type == "folder":
                self._fold[base_name] = True

    def nodes(self):
        self.lazyContain() # Lazy loader
        for filename in self._nodes:
            yield filename

    def children(self):
        self.lazyContain() # Lazy load
        for filename in self._nodes:
            if self._fold[filename]:
                yield filename, RawDirectory(self.dir + "/" + filename)

rootNode = RawDirectory(root)
rootNode.lazyContain()

#
# --------------------------------------------------------------------------------
# == Second Part:
# Raw Directories => Folder Structure
#

# Now I call it folder: it's already in abstract level for the user.
class RawFolder:
    def __init__(self, dir):
        self.dir = dir
        self.contain = False

    def buildDir(self, dir):
        rdir = RawDirectory(dir)
        for filename in rdir.nodes():
            self.nodes[filename] = { "node": rdir._nodes[filename] }

        for filename, child in rdir.children():
            self.children[filename] = child
            self.children[filename]["branch"] = RawFolder(dir + "/" + filename)

    def lazyContain(self):
        if self.contain:
            return
        self.contain = True

        self.children = {}
        self.nodes = {}
        self.root = self.buildDir(self.dir)

for filename in rootNode.children():
    print(filename)


#
# === Agile plan:
#
# We might implement caching and other handling in later versions, where we need to
# optimize - tree.md locations could be cached and the API for the filesystem built
# by other means; files could be watched and their changes noticed. Database could
# be used. The result would be accessible via Anytree, and that's what we are interested
# in: we implement this interface on a low-optimum basis. Let's hope that file tree
# cache works and hard drive is still read once :)
#
# One we update to faster version, the simpler should be maintained as an implementation
# example, where we are interested in keeping the "open source" terms in access to minimal,
# readable and usable version, which can be optimized later as well.
#
# Notice that there are multiple ways of how this could be optimized: perhaps, we would
# implement different ways and create AI cards so that an AI would learn to build this
# system in multiple manners; for example some people would turn off tree.md mapping
# an put their code mostly into a subfolder or have other, separate function to map
# it somewhere. I think this could be achieved even in Apache, directly.
#
# Because we are creating a common standard for Laegna documentations: in case it would
# become a community effort at all, we would have multiple implementations of this format.
#
