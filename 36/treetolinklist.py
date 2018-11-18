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
