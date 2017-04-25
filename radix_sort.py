from collections import defaultdict
from copy import copy

"""
Radix sort implementation for sorting unsigned integers.

TODO: Sorting integers with sings.
"""


def radix_sort(input):
    """ Radix sort implementation for sorting integers"""
    sorted_output = copy(input)
    max_length_item = max(input, key=lambda number: len(str(number)))
    max_length = len(str(max_length_item))

    for i in range(max_length):
        buckets = defaultdict(list)

        for number in sorted_output:
            number_ = str(number)
            digit_index = len(number_) - 1 - i

            if digit_index >= 0:
                key = int(number_[digit_index])
            else:
                key = 0

            buckets[key].append(number)

        sorted_output = []

        for key in range(min(buckets), max(buckets) + 1):
            sorted_output.extend(buckets[key])

    print(sorted_output)
    return sorted_output

if __name__ == '__main__':
    numbers = [511, 522, 533, 677, 899]
    assert radix_sort(numbers) == sorted(numbers)

    numbers = [811, 722, 633, 577, 499]
    assert radix_sort(numbers) == sorted(numbers)

    numbers = [81, 722, 633, 577, 4995]
    assert radix_sort(numbers) == sorted(numbers)
