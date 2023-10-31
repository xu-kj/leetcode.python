def getMinimumFruits(fruits):
    count = {}
    for fruit in fruits:
        if fruit in count:
            count[fruit] += 1
        else:
            count[fruit] = 1

    count = list(count.values())
    while len(count) >= 2:
        count.sort()

        most_common = count.pop()
        second_common = count.pop()
        count.append(abs(most_common - second_common))

    return sum(count)
