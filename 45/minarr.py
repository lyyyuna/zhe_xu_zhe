def compare(a, b):
    ab = a+b
    ba = b+a
    if ab < ba:
        return -1
    elif ab > ba:
        return 1
    else:
        return 0


def getmin(arr):
    arr = [str(elem) for elem in arr]
    arr.sort(compare)

    print arr


getmin([3, 32, 321])