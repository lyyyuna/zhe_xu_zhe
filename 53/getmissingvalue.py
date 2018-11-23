def getMissingValue(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)/2
        if arr[mid] == mid:
            left = mid + 1
        else:
            if mid == 0 or arr[mid-1] == mid-1:
                return mid
            right = mid - 1

    return None


array = [0, 1, 2, 3, 4, 5, 7]
print getMissingValue(array)