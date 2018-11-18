def isPostOrderBST(postorder):
    root = postorder[-1]

    si = 0
    for index, elem in enumerate(postorder):
        if elem > root:
            si = index
            break

    for elem in postorder[si:]:
        if elem < root:
            return False

    left = True
    if si>0:
        left = isPostOrderBST(postorder[:si])
    right = True
    if si<len(postorder)-1:
        right = isPostOrderBST(postorder[si:-1])

    return left and right


print(isPostOrderBST([5, 7, 6, 9, 11, 10, 8]))
print(isPostOrderBST([7, 4, 6, 5]))