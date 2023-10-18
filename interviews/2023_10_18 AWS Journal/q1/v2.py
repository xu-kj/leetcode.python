from typing import List

def transform(nums: List[int]):
    products = [1]
    for number in nums:
        products.append(products[-1] * number)
    products = products[1:]

    products_r = [1]
    for number in nums[::-1]:
        products_r.append(products_r[-1] * number)
    products_r = products_r[1:][::-1]

    result = []
    for i in range(len(nums)):
        r = 1
        if i > 0:
            r *= products[i - 1]
        if i < len(nums) - 1:
            r *= products_r[i + 1]
        result.append(r)

    return result


if __name__ == "__main__":
    print(transform([1, 2, 3, 4]))
    print(transform([1, 2, 3, 4, 0]))
    print(transform([1, 2, 3, 4, 0, 0]))
