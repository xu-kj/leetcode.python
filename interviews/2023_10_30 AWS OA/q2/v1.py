def suitableLocations(centers, d):
    centers.sort()

    left_cumulative_distance = [0]
    for i in range(1, len(centers)):
        curr, prev = centers[i], centers[i - 1]
        distance = left_cumulative_distance[-1] + i * abs(curr - prev) * 2
        left_cumulative_distance.append(distance)

    right_cumulative_distance = [0]
    for i in range(1, len(centers)):
        curr, prev = centers[-1 - i], centers[-1 - i + 1]
        distance = right_cumulative_distance[-1] + i * abs(curr - prev) * 2
        right_cumulative_distance.append(distance)
    right_cumulative_distance = right_cumulative_distance[::-1]

    suitable = []

    # between centers
    for i in range(len(centers) - 1):
        ci, cii = centers[i], centers[i + 1]
        total_distance = left_cumulative_distance[i] + right_cumulative_distance[i + 1]
        for x in range(ci, cii):
            total_ = total_distance
            total_ += (i + 1) * abs(x - ci) * 2
            total_ += (len(centers) - i - 1) * abs(x - cii) * 2
            if total_ <= d:
                suitable.append(x)

    left_suitable = (d - right_cumulative_distance[0]) // 2 if d > right_cumulative_distance[0] else 0
    right_suitable = (d - left_cumulative_distance[-1]) // 2 + 1 if d >= left_cumulative_distance[-1] else 0

    return len(suitable) + left_suitable + right_suitable
