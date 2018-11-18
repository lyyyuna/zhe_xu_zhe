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