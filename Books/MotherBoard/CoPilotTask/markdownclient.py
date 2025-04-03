import os

class Parser():
    def __init__(self):
        self.lines = []
    
    def parse(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    self.lines.append('### ' + line)
                else:
                    self.lines.append(line)
        
        return '\n'.join(self.lines)
