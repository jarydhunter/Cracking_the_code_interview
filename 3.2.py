# Implement a stack that also has a min operation in addition to pop and push, all
# three of which operate in O(1) time.
class myStack:
    def __init__(self):
        self.values = []
    def push(self, item):
        if len(self.values) == 0:
            self.values.append((item,item))
        else:
            self.values.append((item,min(item, self.values[-1][1])))
        return None
    def pop(self, values):
        return self.values.pop()[0]
    def min(self):
        return self.values[1]

