from collections import defaultdict


def bucket_sort(input):
    """Simple and inefficient implementation of bucket sort"""
    number_of_buckets = len(input)
    if number_of_buckets == 1: return input

    output = []
    buckets = defaultdict(list)

    min_value = min(input)
    max_value = max(input)
    q = (max_value - min_value) // number_of_buckets

    for number in input:
        key = (number - min_value) // q
        buckets[key].append(number)

    for key, number in buckets.items():
        if len(buckets[key]):
            rv = bucket_sort(buckets[key])
            output.extend(rv)

    return output



if __name__ == '__main__':
    numbers = [511, 522, 533, 677, 899]
    assert bucket_sort(numbers) == sorted(numbers)

    numbers = [811, 722, 633, 577, 499]
    assert bucket_sort(numbers) == sorted(numbers)

    numbers = [81, 722, 633, 577, 4995]
    assert bucket_sort(numbers) == sorted(numbers)
