from v1 import getMinimumFruits

tcs = [
    ([3, 3, 1, 1, 2], 1),
    ([1, 2, 5, 6], 0),
    ([2, 2, 2, 5, 1, 2], 2),
]

for tc in tcs:
    fruits, expected = tc
    result = getMinimumFruits(fruits)
    print(f"{result=}")
    print(f"{result == expected}")
