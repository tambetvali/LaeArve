
class LuiPages:
    def __init__(self):
        pass

class LuiLink(LuiPages):
    def __init__(self):
        pass

    def setLinkText(self, linktext = "A link"):
        self.linktext = linktext

    # Such as follow automatically, run AI task etc.
    def setLinkAttribute(self, attr, value):
        self.attr = value

class LuiMenu(LuiPages):
    def __init__(self):
        pass