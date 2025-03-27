# Laegna Math Website Architecture: The Folder

# The Folder is used to fold the file system and Documents into the actual structure of our Website, thereby Folding it together.

import os
import re

def xread_from_directory(directory):
    # List all items in the directory, excluding hidden ones (files)
    items = [item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))]
    
    # Define a regular expression to match the file names in the list
    regex = r'\.(jpg|jpeg|png|gif)$'
    
    # Filter and read each file using the regular expression
    files = [os.path.join(directory, filename) for filename in items if os.path.isfile(os.path.join(directory, filename)) and re.search(regex, filename)]
    
    return files

# This is the main class of all our documents, and it's also passed
# to each so that they can send some feedback, for example.
class Documentation:
    pass

# This is a single book, document, nested document etc.
class Document:
    def __init__(self, source):
        self.source = source

class DocumentFolderSource:
    def __init__(self, folder):
        self.folder = folder


        for source in os.listdir(directory):
            print(source)


# Example usage
directory = os.getcwd()
print(os.getcwd())

files = read_from_directory(directory)
print(files)