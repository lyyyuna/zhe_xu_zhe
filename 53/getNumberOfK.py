def getFirstK(arr, start, end, k):
    if start > end:
        return None
    
    midIndex = (start+end)/2
    mid = arr[midIndex]
    if arr[midIndex] == k:
        if midIndex == 0 or arr[midIndex-1] != k:
            return midIndex
        else:
            return getFirstK(arr, start, midIndex-1, k)
    
    if arr[midIndex] < k:
        return getFirstK(arr, midIndex+1, end, k)
    
    if arr[midIndex] > k:
        return getFirstK(arr, start, midIndex-1, k)


def getLastK(arr, start, end, k):
    if start > end:
        return None

    midIndex = (start+end)/2
    mid = arr[midIndex]
    if arr[midIndex] == k:
        if midIndex == len(arr)-1 or arr[midIndex+1] != k:
            return midIndex
        else:
            return getLastK(arr, midIndex+1, end, k)
    
    if arr[midIndex] < k:
        return getLastK(arr, midIndex+1, end, k)

    if arr[midIndex] > k:
        return getLastK(arr, statr, midIndex-1, k)


def getNumberOfK(arr, k):
    firstK = getFirstK(arr, 0, len(arr)-1, k)
    lastK = getLastK(arr, 0, len(arr)-1, k)
    return lastK-firstK+1

  
array = [1, 2, 3, 3, 3, 3, 4, 5]
print getFirstK(array, 0, len(array)-1, 3)
print getNumberOfK(array, 3)