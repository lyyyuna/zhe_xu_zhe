import random

def partition(arr, start, end):
    pivot = random.randint(start, end)
    #print pivot, start, end
    arr[pivot], arr[start] = arr[start], arr[pivot]

    left = start+1
    right = end
    while True:
        while left <= right and arr[left]<=arr[start]:
            left += 1

        while left <= right and arr[right]>=arr[start]:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right


def findMoreThanHalf(arr):
    mid = len(arr)/2
    start = 0
    end = len(arr)-1

    index = partition(arr, start, end)
    while index != mid:
        if index > mid:
            end = index-1
        else:
            start = index+1

        index = partition(arr, start, end)

    return index, arr[index]


print(findMoreThanHalf([1, 2, 3, 2, 2, 2, 5, 4, 2]))


def findMoreThanHalf2(arr):
    res = arr[0]
    cnt = 0
    for index, elem in enumerate(arr):
        if cnt == 0:
            res = elem
        elif res == elem:
            cnt += 1
        elif res != elem:
            cnt -= 1
    return res


print(findMoreThanHalf2([1, 2, 3, 2, 2, 2, 5, 4, 2]))
        
