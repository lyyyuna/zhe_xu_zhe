def getreversepaircnt(arr):
    arrcp = arr[:]
    res = merge(arr, arrcp, 0, len(arr)-1)
    return res


def merge(arr, arrcp, start, end):
    if start == end:
        arrcp[start] = arr[start]
        return 0

    length = (end-start) / 2
    left = merge(arr, arrcp, start, start+length)
    right = merge(arr, arrcp, start+length+1, end)

    cnt = 0
    i = start+length
    j = end
    indexcp = end
    while i >= start and j >= start+length+1:
        if arr[i] > arr[j]:
            cnt += j - start - length
            arrcp[indexcp] = arr[i]
            i -= 1
        else:
            arrcp[indexcp] = arr[j]
            j -= 1
        indexcp -= 1

    while i >= start:
        arrcp[indexcp] = arr[i]
        i -= 1
        indexcp -= 1
    while j >= start+length+1:
        arrcp[indexcp] = arr[j]
        j -= 1
        indexcp -= 1 

    # copy from arrcp to overwrite original array
    for i in range(start, end+1):
        arr[i] = arrcp[i]

    return cnt + left + right


print getreversepaircnt([7, 5, 6, 4])