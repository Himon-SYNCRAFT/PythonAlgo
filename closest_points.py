from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', ['x', 'y'])


def distance(point_a, point_b):
    return sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)

def find_closest_pair(points):
    if len(points) == 2:
        a = points[0]
        b = points[1]
        return distance(a, b), (a, b)

    list_ = sorted(points, key=lambda point: point.x)

    mid  = len(list_) // 2

    left = list_[:mid]
    right = list_[mid:]

    if len(left) < 2:
        min_distance, pair = find_closest_pair(right)
    elif len(right) < 2:
        min_distance, pair = find_closest_pair(left)
    else:
        right_min, right_pair = find_closest_pair(right)
        left_min, left_pair = find_closest_pair(left)

        if left_min <= right_min:
            min_distance = left_min
            pair = left_pair
        else:
            min_distance = right_min
            pair = right_pair

    list_sorted_y = sorted(points, key=lambda point: point.y)

    for index, point in enumerate(list_sorted_y):
        i = 1
        other_index = index + 1

        while i <= 7 and other_index < len(list_sorted_y) - 1:
            other_point = list_sorted_y[other_index]
            other_distance = distance(point, other_point)

            if other_distance < min_distance:
                min_distance = other_distance
                pair = (point, other_point)

            other_index += 1
            i += 1

    return min_distance, pair


if __name__ == '__main__':
    result = distance(Point(2, 3), Point(5, 1))
    assert result == sqrt(13), result

    data = [
        Point(2, 3),
        Point(12, 30),
        Point(40, 50),
        Point(5, 1),
        Point(12, 10),
        Point(3, 4),
    ]

    result = find_closest_pair(data)
    assert result == (1.4142135623730951, (Point(2,3), Point(3,4))), result
