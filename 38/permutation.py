def permutaion(str1, index):
    if len(str1) == index:
        for ch in str1:
            print ch,
        print

    for i in range(index, len(str1)):
        str1[index], str1[i] = str1[i], str1[index]
        permutaion(str1, index+1)
        str1[index], str1[i] = str1[i], str1[index]


permutaion(list('abc'), 0)