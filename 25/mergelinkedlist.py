class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def mergeList(l1, l2):
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    pMergedHead = None

    if l1.value < l2.value:
        pMergedHead = l1
        pMergedHead.next = mergeList(l1.next, l2)
    else:
        pMergedHead = l2
        pMergedHead.next = mergeList(l1, l2.next)

    return pMergedHead


l1_5 = Node(10)
l1_4 = Node(7, l1_5)
l1_3 = Node(5, l1_4)
l1_2 = Node(2, l1_3)
l1_1 = Node(1, l1_2)

l2_3 = Node(6)
l2_2 = Node(6, l2_3)
l2_1 = Node(5, l2_2)
l1_1 = mergeList(l1_1, l2_1)

while l1_1 is not None:
    print l1_1.value
    l1_1 = l1_1.next