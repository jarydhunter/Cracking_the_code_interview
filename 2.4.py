from Linked_lists import linkList
from Linked_lists import Node

# function that will sum two numbers represented as singly linked lists of digits.
# The numbers are assumed to be in base ten.
def sum_lnklsts(lnklst1, lnklst2):
    n1 = lnklst1.head; n2 = lnklst2.head
    sum = n1.value + n2.value
    lnklst_sum = linkList(Node(sum%10))
    carry = sum // 10
    while n1.next.value != None and n2.next.value != None:
        n1 = n1.next; n2 = n2.next
        sum = n1.value + n2.value + carry
        lnklst_sum.append(Node(sum%10))
        carry = sum//10

    if n1.next.value == None:
        long_n = n2
    else:
        long_n = n1

    while long_n.next.value != None:
        sum = long_n.value + carry
        lnklst_sum.append(Node(sum%10))
        carry = sum//10

    # carry must be less than ten since the two lnk lsts were numbers in base
    # ten. If not a safe assumption, then need to change above when adding carry
    # values as well.
    if carry != 0:
        lnklst_sum.append(Node(carry))

    return lnklst_sum

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7]
    test1 = (linkList(Node(values[0])), linkList(Node(9)))
    for v in values[1:]:
        test1[0].append(Node(v));test1[1].append(Node(v))
    for sum in sum_lnklsts(test1[0], test1[1]):
        print(sum.value)



