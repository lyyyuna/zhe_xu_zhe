import heapq


def getmid(arr):
    max_heap = []
    min_heap = []
    for elem in arr:
        if (len(max_heap) + len(min_heap)) % 2 == 0:
            tmp = elem
            if len(max_heap) > 0:
                heapq.heappush(max_heap, -1 * elem)
                tmp = -1 * heapq.heappop(max_heap)
            heapq.heappush(min_heap, tmp)
        else:
            tmp = elem
            if len(min_heap) > 0:
                heapq.heappush(min_heap, elem)
                tmp = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1 * tmp) 

    mid = 0
    if len(arr) % 2 == 0:
        mid = (heapq.heappop(min_heap) + heapq.heappop(max_heap)) / 2
    else:
        mid = -1 * heapq.heappop(max_heap)

    return mid