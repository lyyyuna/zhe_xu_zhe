class BtreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


def createTree(preorder, inorder):
    # precheck
    if not isinstance(preorder, list) or \
        not isinstance(inorder, list) or \
        len(preorder) != len(inorder):
        return

    for x, y in zip(preorder, inorder):
        if not isinstance(x, int) or not isinstance(y, int):
            return
    
    root = construct(preorder, inorder)
    return root


def construct(preorder, inorder):

    if len(preorder) == 0:
        return None

    root = BtreeNode( preorder[0] )
    root_in_index = inorder.index(preorder[0])
    root.left = construct(preorder[1:root_in_index+1], inorder[:root_in_index]) 
    root.right = construct(preorder[root_in_index+1:],inorder[root_in_index+1:])

    return root


def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left, "left")
    print_level(node.right, "right")
    print()
    print(position_name, " ", node.value, end=' ')


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = createTree(preorder, inorder)
    print_level(root, "root")