from v1 import suitableLocations

tcs = [
    ([-2, 1, 0], 8, 3),
    ([2, 0, 3, -4], 22, 5),
    ([-3, 2, 2], 8, 0),
]

for tc in tcs:
    center, d, expected = tc
    result = suitableLocations(center, d)
    print(f"{result=}")
    print(f"{result == expected}")
