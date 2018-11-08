def fibonacci(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    fib0 = 0
    fib1 = 1
    fibn = 0
    while num-2 > 0:
        fibn = fib0 + fib1
        fib0 = fib1
        fib1 = fibn
        num -= 1
    return fibn

print fibonacci(4), fibonacci(5), fibonacci(6)