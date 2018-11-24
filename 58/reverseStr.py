def reverseStr(stri):
    listofstr = list(stri)
    reverse(listofstr, 0, len(listofstr)-1)
    start = 0
    end = 0
    while start < len(listofstr)-1:
        if listofstr[start] == ' ':
            start += 1
            end += 1
        elif listofstr[end] == ' ' or end == len(listofstr)-1:
            reverse(listofstr, start, end-1)
            end += 1
            start = end
        else:
            end += 1

    print "".join(listofstr)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


print reverseStr("Ii am a student.")