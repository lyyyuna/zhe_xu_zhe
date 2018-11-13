class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delNode(headNode, toDelNode):
    if headNode is None or toDelNode is None:
        return None

    if toDelNode.next is not None:
        nextNode = toDelNode.next
        toDelNode.value = nextNode.value
        toDelNode.next = nextNode.next
    elif headNode is toDelNode:
        headNode = None
    else:
        node = headNode
        while node.next is not toDelNode and node.next is not None:
            node = node.next
        node.next = None

    return headNode


l1_5 = Node(10)
l1_4 = Node(7, l1_5)
l1_3 = Node(5, l1_4)
l1_2 = Node(2, l1_3)
l1_1 = Node(1, l1_2)
head_p = l1_1
head_p = delNode(l1_1, l1_2)

while head_p is not None:
    print(head_p.value)
    head_p = head_p.next
