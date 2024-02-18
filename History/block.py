
# This is the main class of Page content
class LaeContentBlock:
    def __init__(self):
        self.setTitle()
        self.blocks = []

    def setTitle(self, title="", subtitle="", visibility=True):
        self.title = title
        self.subtitle = subtitle

    def addBlock(self, block):
        self.blocks.append(block)
