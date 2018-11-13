def cut(length):
    if length == 1:
        return 1
    if length == 2:
        return 2
    if length == 3:
        return 2

    products = [0 for _ in range(length + 1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, length+1):
        for j in range(1, i/2+1):
            product = products[j] * products[i-j]
            if product > products[i]:
                products[i] = product
    return products[length]


print cut(5), cut(3)    