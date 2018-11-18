class ComplexNode():
    def __init__(self, value, next, sibling):
        self.value = value
        self.next = next
        self.sibling = sibling


def cloneNodes(pHead):
    pNode = pHead
    while pNode:
        cloneNode = ComplexNode()
        cloneNode.next = pNode.next
        pNode.next = cloneNode
        cloneNode.value = pNode.value
        pNode = cloneNode.next


def connectSiblingNodes(pHead):
    pNode = pHead
    while pNode:
        pClone = pNode.next
        if pNode.sibling:
            pClone.sibling = pNode.sibling.next
        pNode = pClone.next


def reconnectNodes(pHead):
    pNode = pHead
    pClone = pHead.next
    pCloneHead = pClone

    pNode.next = pClone.next
    pNode = pNode.next

    while pNode:
        pClone.next = pNode.next
        pClone = pClone.next

        pNode.next = pClone.next
        pNode = pNode.next

    return pCloneHead
