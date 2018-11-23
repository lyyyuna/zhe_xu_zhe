def getugly(index):
    uglyarr = [0] * index
    ugly2index = 0
    ugly3index = 0
    ugly5index = 0
    uglyindex = 0

    uglyarr[0] = 1
    uglyindex += 1

    while uglyindex < index:
        uglyarr[uglyindex] = min(uglyarr[ugly2index] * 2,
                                uglyarr[ugly3index] * 3,
                                uglyarr[ugly5index] * 5)
        while uglyarr[ugly2index] * 2 <= uglyarr[uglyindex]:
            ugly2index += 1
        while uglyarr[ugly3index] * 3 <= uglyarr[uglyindex]:
            ugly3index += 1
        while uglyarr[ugly5index] * 5 <= uglyarr[uglyindex]:
            ugly5index += 1

        uglyindex += 1

    return uglyarr[-1]


def isUgly(num):
    while num%2==0:
        num /= 2
    while num%3==0:
        num /= 3
    while num%5==0:
        num /= 5
    if num == 1:
        return True
    else:
        return False


print getugly(1500)
print isUgly(getugly(1500))