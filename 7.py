def print_(num, begin, end):
    if begin >= end:
        print num
    j = begin
    for i in range(begin, end):
        num[i], num[j] = num[j], num[i]
        print_(num, begin+1, end)
        num[i], num[j] = num[j], num[i]

print_(list('abc'), 0, len('abc'))