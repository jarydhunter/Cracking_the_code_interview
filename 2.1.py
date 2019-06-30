from Linked_lists import linkList
from Linked_lists import Node

# Remove duplicates from a linked list. Challenge for another time, implement
# this with no seen object.
def rmv_dups(lnklst):
    seen = set()
    for elem in lnklst:
        if not elem.value in seen:
            seen.add(elem.value)
        else:
            elem.prev.next = elem.next
            elem.next.prev = elem.prev
    return lnklst


if __name__ == '__main__':
    values = [1,2,3,4,5,6,7]
    test1 = linkList(Node(values[0]))
    for v in values[1:]:
        test1.append(Node(v))
    rmv_dups(test1)
    for node in test1:
        print(node.value)
    print('end of test1')

    values = [1, 2, 3, 4, 1, 5, 6, 7, 1]
    test2 = linkList(Node(values[0]))
    for v in values[1:]:
        test2.append(Node(v))
    rmv_dups(test2)
    for node in test2:
        print(node.value)
    print('end of test2')

