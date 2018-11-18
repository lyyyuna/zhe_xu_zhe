def isPopOrder(push_order, pop_order):
    pushIndex = 0
    popIndex = 0
    stack = []

    while popIndex <= len(pop_order)-1:
        while not stack or stack[-1] != pop_order[popIndex]:
            if pushIndex > len(push_order)-1:
                break
            stack.append(push_order[pushIndex])
            pushIndex += 1
        if stack[-1] != pop_order[popIndex]:
            return False

        # equal
        popIndex += 1
        stack.pop()

    return True


print(isPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(isPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
