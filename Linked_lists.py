# Personal implementation of a linked list, to be used in chapter 2 questions.

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    def __next__(self):
        if self.value == None:
            raise StopIteration
        return self.next
    def __iter__(self):
        return self

class linkList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.head.next = Node()
        self.head.prev = Node()
    def append(self, node):
        node.next = self.tail.next
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    def __next__(self):
        tmp = self.cur
        self.cur = self.cur.__next__()
        return tmp
    def __iter__(self):
        self.cur = self.head
        return self

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    lnk = linkList(n1)
    lnk.append(n2)
    lnk.append(n3)

    for node in lnk:
        print(node.value)