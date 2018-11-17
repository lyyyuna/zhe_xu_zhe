class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def findReverseKNode(pHead, k):
    p1 = pHead
    p2 = pHead

    for _ in range(k):
        p1 = p1.next
        if p1 == None:
            return None

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2
    


l1_5 = Node(5)
l1_4 = Node(4, l1_5)
l1_3 = Node(3, l1_4)
l1_2 = Node(2, l1_3)
l1_1 = Node(1, l1_2)
head = l1_1

print findReverseKNode(head, 2).value
print findReverseKNode(head, 1).value