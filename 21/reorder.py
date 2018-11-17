def reorder(arr):
    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:
        while p1 < p2 and isOdd(arr[p1]):
            p1 += 1

        while p1 < p2 and isEven(arr[p2]):
            p2 -= 1

        arr[p1], arr[p2] = arr[p2], arr[p1]


def isOdd(n):
    return n%2 == 1


def isEven(n):
    return n%2 == 0


nums = [1, 2, 3, 4, 5]
reorder(nums)
print nums