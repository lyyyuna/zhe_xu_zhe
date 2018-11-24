def findNumAppearOnce(arr):
    tmp = 0
    for ch in arr:
        tmp ^= ch
    index = findFirstBitOne(tmp)
    tmp = 1 << index

    num1 = 0
    num2 = 0
    for ch in arr:
        if ch & tmp:
            num1 ^= ch
        else:
            num2 ^= ch
    return num1, num2


def findFirstBitOne(num):
    index = 0
    while num and num & 1 == 0:
        index += 1
        num = num >> 1

    return index


def findNumAppearOnce2(arr):
    bitSum = [0] * 32
    for elem in arr:
        bitMask = 1
        for i in range(31, -1, -1):
            if elem & bitMask:
                bitSum[i] += 1
            bitMask <<= 1

    res = 0
    for elem in bitSum:
        res <<= 1
        res += elem%3
    return res


print findNumAppearOnce([-8, -4, 3, 6, 3, -8, 5, 5])
print findNumAppearOnce2([2, 18, 3, 7, 3, 3, 2, 7, 2, 7])