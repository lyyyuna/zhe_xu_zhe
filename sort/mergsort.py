def merge(arr1, arr2):
    mergeRes = []
    arr1Index = arr2Index = 0

    while arr1Index < len(arr1) and arr2Index < len(arr2):
        if arr1[arr1Index] < arr2[arr2Index]:
            mergeRes.append(arr1[arr1Index])
            arr1Index += 1

        else:
            mergeRes.append(arr2[arr2Index])
            arr2Index += 1

    if arr1Index == len(arr1):
        for i in arr2[arr2Index:]:
            mergeRes.append(i)
    else:
        for i in arr1[arr1Index:]:
            mergeRes.append(i)

    return mergeRes


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)/2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)        


print mergeSort([4, 7, 8, 3, 5, 9])