from heapq import heapify, heappop, heappush
from itertools import count


def huffman(sequence, frequencies):
    num = count()
    trees = list(zip(frequencies, num, sequence))
    heapify(trees)

    while len(trees) > 1:
        frequency_a, _, a = heappop(trees)
        frequency_b, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (frequency_a + frequency_b, n, [a, b]))

    return trees[0][-1]


if __name__ == '__main__':
    sequence = 'abcdefghi'
    frequencies = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    result = huffman(sequence, frequencies)
    print(result)
