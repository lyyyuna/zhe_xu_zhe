def qsort(arr):
    if len(arr) <= 1:
        return arr

    return qsort([x for x in arr[1:] if x < arr[0]]) +\
           [arr[0]] +\
           qsort([x for x in arr[1:] if x >= arr[0]])


print qsort([4, 7, 8, 3, 5, 9])