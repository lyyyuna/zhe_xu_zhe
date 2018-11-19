import random


def partition(arr, start, end):
    pivot = random.randint(start, end)
    arr[pivot], arr[start] = arr[start], arr[pivot]

    left = start+1
    right = end

    while True:
        while left <= right and arr[left] <= arr[start]:
            left += 1

        while left <= right and arr[right] >= arr[start]:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]

    return right


def getkmin(arr, k):
    start = 0
    end = len(arr)-1
    index = partition(arr, start, end)
    while index != k-1:
        if index > k-1:
            end = index-1
        else:
            start = index+1
        index = partition(arr, start, end)

    for i in range(k):
        print arr[i],


getkmin([4, 5, 1, 6, 2, 7, 3, 8], 4)

print
import heapq


def getkmin2(arr, k):
    max_heap = []
    for x in arr:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    for x in max_heap:
        print -x,


getkmin2([4, 5, 1, 6, 2, 7, 3, 8], 4)
