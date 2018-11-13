def findMinInRotatedArr(arr):
    index1 = 0
    index2 = len(arr)-1
    while arr[index1] > arr[index2]:
        if index2-index1 == 1:
            indexMid = index2
            break
        indexMid = (index1+index2)/2
        if arr[indexMid] >= arr[index1]:
            index1 = indexMid
        if arr[indexMid] <= arr[index2]:
            index2 = indexMid
    return arr[indexMid]


print(findMinInRotatedArr([3, 4, 5, 1, 2]))