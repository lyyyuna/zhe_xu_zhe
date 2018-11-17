class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverseLinkList(pHead):
    pReversedHead = None
    pPrev = None
    pNode = pHead

    while pNode is not None:
        pNext = pNode.next
        if pNext is None:
            pReversedHead = pNode

        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext

    return pReversedHead


l1_6 = Node(6)
l1_5 = Node(5, l1_6)
l1_4 = Node(4, l1_5)
l1_3 = Node(3, l1_4)
l1_2 = Node(2, l1_3)
l1_1 = Node(1, l1_2)
head = l1_1

p = reverseLinkList(head)
while p:
    print p.value
    p = p.next