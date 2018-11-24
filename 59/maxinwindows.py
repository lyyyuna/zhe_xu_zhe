from collections import deque


def maxInWindow(arr, winsize):
    maxOfWindow = []
    indexQueue = deque()

    for i in range (winsize):
        while len(indexQueue) != 0 and arr[indexQueue[-1]] < arr[i]:
            indexQueue.pop()
        indexQueue.append(i) 

    for i in range(winsize, len(arr)):
        maxOfWindow.append(arr[indexQueue[0]])

        while len(indexQueue) != 0 and arr[indexQueue[-1]] < arr[i]:
            indexQueue.pop()

        if len(indexQueue) != 0 and indexQueue[0] + winsize <= i:
            indexQueue.popleft()
        indexQueue.append(i)
    maxOfWindow.append(arr[indexQueue[0]])
    return maxOfWindow


print maxInWindow([2, 3, 4, 2, 6, 2, 5, 1], 3)