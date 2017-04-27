from math import inf as infinity
from heapq import heapify, heappop, heappush
from collections import namedtuple


WeightedEdge = namedtuple('WeightedEdge', ['weight', 'parent', 'child'])


def prims(graph, s):
    min_heap = [WeightedEdge(weight=0, parent=None, child=s)]
    result = {}

    while min_heap:
        edge = heappop(min_heap)
        if edge.child in result:
            continue
        result[edge.child] = edge.parent

        for child, weight in graph[edge.child].items():
            heappush(min_heap,(WeightedEdge(weight=weight,parent=edge.child,
                                           child=child)))

    return [WeightedEdge(graph[parent][child], parent, child)
            for parent, child in result.items() if child is not None]


if __name__ == '__main__':
    graph = {
        'A': {
            'B': 2,
            'D': 3,
            'C': 3,
        },
        'B': {
            'A': 2,
            'E': 3,
            'C': 4,
        },
        'C': {
            'A': 3,
            'B': 4,
            'D': 5,
            'E': 1,
            'F': 6,
        },
        'D': {
            'A': 3,
            'F': 7,
            'C': 5,
        },
        'E': {
            'C': 1,
            'F': 8,
            'B': 3,
        },
        'F': {
            'E': 8,
            'D': 7,
            'G': 9,
            'C': 6,
        },
        'G': {
            'F': 9,
        },
    }

    result = prims(graph, 'A')
    print(result)

    total_weight = 0

    for weight, _, _ in result:
        total_weight += weight

    assert total_weight == 24
