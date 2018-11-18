class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def serialize(pRoot):
    if pRoot is None:
        return

    print pRoot.value,
    if pRoot.left_child:
        serialize(pRoot.left_child)
    else:
        print '$',

    if pRoot.right_child:
        serialize(pRoot.right_child)
    else:
        print '$',


def deserialize(arr):
    node = None
    if arr[0] == '$':
        node = None
    else:
        node = TreeNode(value=arr[0])

    arr.popleft()

    if node:
        node.left_child = deserialize(arr)
        node.right_child = deserialize(arr)
    return node