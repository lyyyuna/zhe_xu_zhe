class TreeNode():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


from collections import deque
def printBinaryTree(pRoot):
    if pRoot is None:
        return

    d = deque()
    d.append(pRoot)
    nextLevelNum = 0
    currentLevelNum = 1
    while d:
        pNode = d.popleft()
        print pNode.value, 
        if pNode.left_child:
            d.append(pNode.left_child)
            nextLevelNum += 1
        if pNode.right_child:
            d.append(pNode.right_child)
            nextLevelNum += 1

        currentLevelNum -= 1
        if currentLevelNum == 0:
            print 
            currentLevelNum = nextLevelNum
            nextLevelNum = 0


node7 = TreeNode(11)
node6 = TreeNode(9)
node5 = TreeNode(7)
node4 = TreeNode(5)
node3 = TreeNode(10, left_child=node6, right_child=node7)
node2 = TreeNode(6, left_child=node4, right_child=node5)
node1 = TreeNode(8, left_child=node2, right_child=node3)
root = node1

printBinaryTree(root)
