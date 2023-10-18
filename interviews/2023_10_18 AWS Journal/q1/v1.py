from typing import List

def transform(nums: List[int]):
    nzero = []
    product = 1
    for i, number in enumerate(nums):
        if number == 0:
            nzero.append(i)
        else:
            product *= number
            
    if len(nzero) > 1:
        return [0] * len(nums)
    elif len(nzero) == 1:
        result = [0] * len(nums)
        result[nzero[0]] = product
        return result
    else:
        return [product / num for num in nums]


if __name__ == "__main__":
    print(transform([1, 2, 3, 4]))
    print(transform([1, 2, 3, 4, 0]))
    print(transform([1, 2, 3, 4, 0, 0]))
