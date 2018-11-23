class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def treeDepth(pRoot):
    if pRoot is None:
        return 0

    left = treeDepth(pRoot.left_child)
    right = treeDepth(pRoot.right_child)
    return max(left, right)+1


def isBalanced(pRoot):
    if pRoot is None:
        return True, 0

    leftB, leftD = isBalanced(pRoot.left_child)
    rightB, rightD = isBalanced(pRoot.right_child)
    if leftB and rightB:
        diff = abs(leftD-rightD)
        if diff <= 1:
            depth = max(leftD, rightD) + 1
            return True, depth
    
    return False, 0
            
    


node7 = TreeNode(7)
node6 = TreeNode(6)
node5 = TreeNode(5, node7)
node4 = TreeNode(4)
node3 = TreeNode(3, None, node6)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)
root = node1

print treeDepth(root)
print isBalanced(root)
