def consistentSum(arr):
    sum = 0
    maxsum = 0
    for elem in arr:
        if sum < 0:
            sum = elem
        else:
            sum += elem

        if sum > maxsum:
            maxsum = sum

    return maxsum


print(consistentSum([1, -2, 3, 10, -4, 7, 2, -5]))