def printToMaxOfNDigits(num):
    if num <= 0:
        return
    digits = [0] * num
    printDigitsRecursivly(digits, num, 0)


def printDigitsRecursivly(digits, length, index):
    if index == length:
        print int(''.join(digits))
        return

    for i in range(10):
        digits[index] = str(i)
        printDigitsRecursivly(digits, length, index+1)


def printDigits(digits):
    pass


printToMaxOfNDigits(5)