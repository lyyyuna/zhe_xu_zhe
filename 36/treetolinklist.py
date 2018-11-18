class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def convert(pRoot):
    plast = None
    plast = convertdfs(pRoot, plast)
    while plast and plast.left_child:
        plast = plast.left_child
    return plast


def convertdfs(pCur, pLast):
    if pCur is None:
        return None

    if pCur.left_child:
        pLast = convertdfs(pCur.left_child, pLast)

    if pLast:
        pLast.right_child = pCur
        pCur.left_child = pLast
    pLast = pCur

    if pCur.right_child:
        pLast = convertdfs(pCur.right_child, pLast)

    return pLast


node7 = TreeNode(16)
node6 = TreeNode(12)
node5 = TreeNode(8)
node4 = TreeNode(4)
node3 = TreeNode(14, left_child=node6, right_child=node7)
node2 = TreeNode(6, left_child=node4, right_child=node5)
node1 = TreeNode(10, left_child=node2, right_child=node3)
root = node1

head = convert(root)
while head:
    print head.value,
    head = head.right_child


def dfs(pCur, pLast):
    if pCur.left_child:
        pLast = dfs(pCur.left_child, pLast)

    if pLast:
        pLast.right_child = pCur
        pCur.left_child = pLast

    pLast = pCur

    if pCur.right_child:
        pLast = dfs(pCur.right_child, pLast)

    return pLast