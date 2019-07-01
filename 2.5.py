from Linked_lists import linkList
from Linked_lists import Node

#Detect circular portion of a linked list. This solution I don't think is as
# good as the one in the book, since adding to a dictionary is amortized O(1)
# this algo is amortized O(n), but the books solution I think is worst case O(n).
# I think a simple way to make this algo more useful would be to return the last
# element of the loop, then you have the node the correct node that has the
# broken next, otherwise you have to go around the loop again which could be
# another n time.
def get_loop_slow(lnklst):
    seen = {}
    for n in lnklst:
        seen[id(n)] = True
        if id(n.next) in seen:
            return n.next

def get_loop_better(lnklst):
    n1 = lnklst.head.next
    n2 = lnklst.head.next.next
    i = 1
    while n1 != n2 and n2.next is not None and n2.next.next is not None:
        n1 = n1.next
        n2 = n2.next.next
        i += 1
    if n1 == n2:
        n1 = lnklst.head
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next
        return n1
    else:
        return None

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7]
    test1 = linkList(Node(values[0]))
    for v in values[1:]:
        test1.append(Node(v))
    # Make list corrupt
    test1.head.next.next = test1.head
    print(get_loop_slow(test1).value)
    print(get_loop_better(test1).value)

