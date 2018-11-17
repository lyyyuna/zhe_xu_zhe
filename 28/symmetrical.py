class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def issym(pRoot1, pRoot2):
    if pRoot1 is None and pRoot2 is None:
        return True

    if pRoot1 is None or pRoot2 is None:
        return False

    if pRoot1.value != pRoot2.value:
        return False

    return issym(pRoot1.left_child, pRoot2.right_child) and\
           issym(pRoot1.right_child, pRoot2.left_child)


node7 = TreeNode(5)
node6 = TreeNode(7)
node5 = TreeNode(7)
node4 = TreeNode(5)
node3 = TreeNode(9, left_child=node6, right_child=node7)
node2 = TreeNode(6, left_child=node4, right_child=node5)
node1 = TreeNode(8, left_child=node2, right_child=node3)
root = node1

print issym(root, root)


node7 = TreeNode(5)
node6 = TreeNode(7)
node5 = TreeNode(7)
node4 = TreeNode(5)
node3 = TreeNode(6, left_child=node6, right_child=node7)
node2 = TreeNode(6, left_child=node4, right_child=node5)
node1 = TreeNode(8, left_child=node2, right_child=node3)
root = node1

print issym(root, root)


node6 = TreeNode(7)
node5 = TreeNode(7)
node4 = TreeNode(7)
node3 = TreeNode(7, left_child=node6)
node2 = TreeNode(7, left_child=node4, right_child=node5)
node1 = TreeNode(7, left_child=node2, right_child=node3)
root = node1

print issym(root, root)
