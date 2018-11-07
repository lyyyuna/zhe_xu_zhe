class TreeNode():
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def createTree(preorder, inorder):
    if len(preorder) == 0:
        return None

    root_value = preorder[0]
    root_index = inorder.index(root_value)

    rootNode = TreeNode(root_value)
    rootNode.left_node = createTree(preorder[1:root_index+1], inorder[:root_index])
    rootNode.right_node = createTree(preorder[root_index+1:], inorder[root_index+1:])

    return rootNode


def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left_node, "left")
    print_level(node.right_node, "right")
    print()
    print position_name, " ", node.data,


preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
root = createTree(preorder=preorder, inorder=inorder)
print_level(root, "root")



