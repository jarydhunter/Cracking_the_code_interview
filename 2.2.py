from Linked_lists import linkList
from Linked_lists import Node

# Get nth last element of a single linked list, i.e. don't use the prev
# attribute I implemented. If n = 0 it will return the last element in the list,
# n= 1 will return the second last element, etc...
def get_n_last(lnklst, n):
    i = 0
    n_last = lnklst.head
    last = lnklst.head
    while i < n and last.next.value != None:
        last = last.next
        i += 1
    while last.next.value != None:
        n_last = n_last.next
        last = last.next
    return n_last

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7]
    test1 = linkList(Node(values[0]))
    for v in values[1:]:
        test1.append(Node(v))
    print(get_n_last(test1, 2).value)