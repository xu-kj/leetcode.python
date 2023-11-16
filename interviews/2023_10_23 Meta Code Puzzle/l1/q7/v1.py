# Write any import statements here


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    digits_A, digits_B = getNumberOfDigits(A), getNumberOfDigits(B)
    ub_A, ub_B = getUniformBase(digits_A), getUniformBase(digits_B)

    if digits_B > digits_A:
        result = 0
        result += 9 - (A - 1) // ub_A
        result += B // ub_B
        result += 9 * (digits_B - digits_A - 1)
    else:
        result = 0
        result += B // ub_B - (A - 1) // ub_A

    return result


def getNumberOfDigits(number: int) -> int:
    digits = 0

    while number:
        digits += 1
        number //= 10

    return digits


def getUniformBase(digits: int) -> int:
    result = 0
    for _ in range(digits):
        result *= 10
        result += 1

    return result
