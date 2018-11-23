def findFirstOnceChar(stri):
    cnt = {}

    for ch in stri:
        if ch not in cnt:
            cnt[ch] = 1
        else:
            cnt[ch] += 1

    for ch in stri:
        if cnt[ch] == 1:
            return ch

    return None


print findFirstOnceChar("abaccdeff")