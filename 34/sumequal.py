class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def sumEqual(pRoot, expected, path, currentsum):
    currentsum += pRoot.value
    path.append(pRoot)
    if pRoot.left_child is None and pRoot.right_child is None and\
        currentsum == expected:
        for node in path:
            print node.value,
        print
        #return

    if pRoot.left_child is not None:
        sumEqual(pRoot.left_child, expected, path, currentsum)
    if pRoot.right_child is not None:
        sumEqual(pRoot.right_child, expected, path, currentsum)

    path.pop()


def find_path(root, expected_sum):
    if not isinstance(root, TreeNode) or not isinstance(expected_sum, int):
        return

    path = []
    current_sum = 0
    find_path_core(root, expected_sum, path, current_sum)


def find_path_core(root, expected_sum, path, current_sum):
    path.append(root)
    current_sum += root.value
    if root.left_child is None and root.right_child is None and current_sum == expected_sum:
        print((",".join([str(n.value) for n in path])))

    if root.left_child is not None:
        find_path_core(root.left_child, expected_sum, path, current_sum)

    if root.right_child is not None:
        find_path_core(root.right_child, expected_sum, path, current_sum)

    path.pop()


node5 = TreeNode(7)
node4 = TreeNode(4)
node3 = TreeNode(12)
node2 = TreeNode(5, node4, node5)
node1 = TreeNode(10, node2, node3)
root = node1

sumEqual(root, 22, [], 0)

find_path(root, 22)