def replacespace(str1):
    str1 = list(str1)
    p1 = len(str1)-1
    for s in str1:
        if s == ' ':
            str1.append(None)
            str1.append(None)

    p2 = len(str1)-1

    while p1 != p2:
        if str1[p1] != ' ':
            str1[p2] = str1[p1]
            p2 -= 1
        else:
            str1[p2-2:p2+1] = '%20'
            p2 -= 3
        p1 -= 1
    
    return ''.join(str1)


print replacespace('HLLO   WW')


    