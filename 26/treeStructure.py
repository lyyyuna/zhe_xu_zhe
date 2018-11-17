class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.leftnode = left_child
        self.rightnode = right_child


def hasSameRoot(pRoot1, pRoot2):
    result = False
    if pRoot1 is not None and pRoot2 is not None:
        if pRoot1.value == pRoot2.value:
            result = hasSameStructure(pRoot1, pRoot2)
        if result is not True:
            result = hasSameRoot(pRoot1.leftnode, pRoot2)
        if result is not True:
            result = hasSameRoot(pRoot1.rightnode, pRoot2)

    return result


def hasSameStructure(pRoot1, pRoot2):
    if pRoot2 is None:
        return True

    if pRoot1 is None:
        return False

    if pRoot1.value != pRoot2.value:
        return False

    return hasSameStructure(pRoot1.leftnode, pRoot2.leftnode) and\
            hasSameStructure(pRoot1.rightnode, pRoot2.rightnode)

    
tree1_7 = TreeNode(value=7)
tree1_6 = TreeNode(value=4)
tree1_5 = TreeNode(value=2, left_child=tree1_6, right_child=tree1_7)
tree1_4 = TreeNode(value=9)
tree1_3 = TreeNode(value=7)
tree1_2 = TreeNode(value=8, left_child=tree1_4, right_child=tree1_5)
tree1_1 = TreeNode(value=8, left_child=tree1_2, right_child=tree1_3)
tree1 = tree1_1

tree2_3 = TreeNode(2)
tree2_2 = TreeNode(9)
tree2_1 = TreeNode(8, left_child=tree2_2, right_child=tree2_3)
tree2 = tree2_1


print hasSameRoot(tree1, tree2)