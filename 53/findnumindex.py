def findNumEqualIndex(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)/2
        if arr[mid] < mid:
            left = mid+1
        if arr[mid] > mid:
            right = mid-1
        if arr[mid] == mid:
            return mid

    return None


array = [-3, -1, 1, 3, 5]
print findNumEqualIndex(array)