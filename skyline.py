from collections import deque


def make_skyline(buildings):
    result = deque()

    for left, height, right in buildings:
        building = deque()
        building.append((left, height))
        building.append((right, 0))
        result.append(building)

    while len(result) > 1:
        a = result.popleft()
        b = result.popleft()
        skyline = deque()
        height_a, height_b = 0, 0

        while a and b:
            if a[0][0] <= b[0][0]:
                point = a.popleft()
                x, height_a = point
            else:
                point = b.popleft()
                x, height_b = point

            curr_height = height
            height = max(height_a, height_b)

            if curr_height != height:
                skyline.append((x, height))

        skyline.extend(a)
        skyline.extend(b)

        result.append(skyline)

    result = [point for skyline in result for point in skyline]

    return result



if __name__ == '__main__':
    assert make_skyline([]) == []

    buildings = [(1, 11, 5)]
    result = make_skyline(buildings)
    assert result == [(1, 11), (5, 0)], result

    buildings = [(1, 11, 5), (3, 5, 8)]
    result = make_skyline(buildings)
    assert result == [(1, 11), (5, 5), (8, 0)], result

    buildings = [(1, 11, 5), (2, 6, 7), (3, 13, 9),
                 (12, 7, 16), (14, 3, 25), (19, 18, 22),
                 (23, 13, 29), (24, 4, 28)]
    result = make_skyline(buildings)
    assert result == [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3),
                      (19, 18), (22, 3), (23, 13), (29, 0)], result
