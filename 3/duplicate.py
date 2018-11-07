def duplicate(numbers):
    if not isinstance(numbers, list):
        return False

    for num in numbers:
        if not isinstance(num, int):
            return False

    for index in range(len(numbers)):
        while number in 