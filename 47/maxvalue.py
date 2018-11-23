def getMaxValue(arr):
    rowNum = len(arr)
    colNum = len(arr[0])

    maxArr = [[0] * colNum for _ in arr ]
    for i in range(rowNum):
        for j in range(colNum):
            up = 0
            left = 0

            if i > 0:
                up = maxArr[i-1][j]
            if j > 0:
                left = maxArr[i][j-1]
            maxArr[i][j] = arr[i][j] + max(up, left)
    return maxArr[-1][-1]


m = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
print getMaxValue(m)