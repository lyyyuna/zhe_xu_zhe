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


print getugly(1500)