# Implement SetOfStacks where there is a max height for stacks i.e. the whole
# stack can be stored in a sort of linked list of stacks.

class SetOfStacks:
    def __init__(self, max_height):
        self.max_height = max_height
        self.stacks = []
    def push(self, item):
        if not self.stacks: # Pythonic way of checking for empty list.
            self.stacks[0] = [item]
        elif len(self.stacks[-1]) < self.max_height:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    def pop(self):
        if not self.stacks:
            return None
        elif not self.stacks[-1]:
            self.stacks.pop()
            return self.stacks[-1].pop()
        else:
            return self.stacks[-1].pop()
