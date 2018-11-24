def findSum(arr, num):
    start = 0
    end = len(arr)-1

    sum = 0
    
    while start < end:
        sum = arr[start] + arr[end]
        if sum < num:
            start += 1
        if sum > num:
            end -= 1
        if sum == num:
            return True, arr[start], arr[end]

    return False, None, None


print findSum([1, 2, 4, 7, 11, 15], 15)


def findSum2(num):
    start = 1
    end = 2
    mid = (num + 1) / 2
    while start < mid:
        seq = [x for x in range(start, end+1)]
        if sum(seq) == num:
            print seq
            start += 1
        if sum(seq) > num:
            start += 1
        if sum(seq) < num:
            end += 1


print findSum2(15)


