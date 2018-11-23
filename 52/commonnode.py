class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def getLength(pHead):
    length = 0
    pNode = pHead
    while pNode:
        pNode = pNode.next
        length += 1
    return length


def findFirstCommonNode(pHead1, pHead2):
    len1 = getLength(pHead1)
    len2 = getLength(pHead2)

    pLong = pHead1
    pShort = pHead2
    delta = len1 - len2
    if len1 < len2:
        pLong = pHead2
        pShort = pHead1
        delta = len2 - len1

    while delta:
        pLong = pLong.next
        delta -= 1

    while pLong and pShort and pLong is not pShort:
        pLong = pLong.next
        pShort = pShort.next

    return pLong


node7 = Node(7)
node6 = Node(6, node7)
node5 = Node(5, node6)
node4 = Node(4, node5)
head2 = node4

node3 = Node(3, node6)
node2 = Node(2, node3)
node1 = Node(1, node2)
head1 = node1

pCommon = findFirstCommonNode(head1, head2)
print pCommon.value
            