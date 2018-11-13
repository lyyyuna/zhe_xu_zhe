def power(base, exponent):
    if base == 0 and exponent == 0:
        return None
    flag = False
    if exponent < 0:
        flag = True
        exponent = abs(exponent)

    res = 1
    for i in range(exponent):
        res *= base

    if flag:
        res = 1.0/res
    return res 
    