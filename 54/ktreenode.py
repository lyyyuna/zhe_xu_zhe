class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def ktreenode(pRoot, k):
    value = None
    if pRoot.left_child is not None:
        value, k = ktreenode(pRoot.left_child, k)

    if value == None:
        if k==1:
            value = pRoot.value
        k -= 1
    
    if value is None and pRoot.right_child is not None:
        value, k = ktreenode(pRoot.right_child, k)

    return value, k


node8 = TreeNode(8)
node6 = TreeNode(6)
node4 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3, node2, node4)
node7 = TreeNode(7, node6, node8)
node5 = TreeNode(5, node3, node7)
root = node5

print ktreenode(root, 3)