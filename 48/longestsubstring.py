def longestsubstring(stri):
    maxLength = 0
    curLength = 0
    position = [-1] * 26

    for index, ch in enumerate(stri):
        prevIndex = position[ord(ch) - ord('a')]
        if prevIndex < 0 or index-prevIndex > curLength:
            curLength += 1
        else:
            curLength = index - prevIndex

        if curLength > maxLength:
            maxLength = curLength

        position[ord(ch) - ord('a')] = index
    return maxLength


print longestsubstring("arabcacfr")
