from math import inf as infinity
from heapq import heapify, heappop, heappush
from collections import namedtuple


"""
Prim's Algorithm for finding minimum spanning tree in graph

1. Choose a node to start traversing
2. Loop:
    1. Add node's children to the min_heap
    2. If node not visited add edge from node you came from
    3. Get child whose edge has smallest weight
"""


WeightedEdge = namedtuple('WeightedEdge', ['weight', 'node_from', 'node_to'])


def prims(graph):
    # node to start from
    start = next(iter(graph))
    min_heap = [WeightedEdge(weight=0, node_from=None, node_to=start)]
    result = {}

    while min_heap:
        _, node_from, node_to = heappop(min_heap)
        if node_to in result:
            continue
        result[node_to] = node_from

        for child, weight in graph[node_to].items():
            heappush(min_heap, WeightedEdge(weight, node_to, child))

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

    result = prims(graph)

    total_weight = 0

    for weight, _, _ in result:
        total_weight += weight

    assert total_weight == 24, total_weight

