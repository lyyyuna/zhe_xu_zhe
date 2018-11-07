class TreeNode():
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


def set_relation(parent, left_child, right_child):
    parent.left = left_child
    parent.right = right_child
    left_child.parent = parent
    right_child.parent = parent


def find_next_node(node):
    if node is None:
        return None

    # if this node has a right node
    if node.right:
        next_node = node.right
        while next_node.left:
            next_node = next_node.left
        return next_node

    # if this node has parent
    if node.parent:
        parent = node.parent
        # if this node is left child of parent
        if node.parent.left is node:
            return node.parent

        # if this node is right child of parent
        if node.parent.right is node:
            while parent.parent:
                if parent is parent.parent.left:
                    return parent.parent
                parent = parent.parent

    return None
    



node_i = TreeNode("i")
node_h = TreeNode("h")
node_g = TreeNode("g")
node_f = TreeNode("f")
node_e = TreeNode("e")
node_d = TreeNode("d")
node_c = TreeNode("c")
node_b = TreeNode("b")
node_a = TreeNode("a")
set_relation(node_e, node_h, node_i)
set_relation(node_c, node_f, node_g)
set_relation(node_b, node_d, node_e)
set_relation(node_a, node_b, node_c)

print find_next_node(node_i).data