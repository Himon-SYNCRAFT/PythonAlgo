from collections import namedtuple


"""
Kruskal Algorithm for finding minimum spanning tree in graph

1. Extract Edges from Graph and sort them by weight
2. Iterate over sorted edges
3. If edge not create a cycle, add it to the result

For finding if edge create a cycle we use find_union algorithm:
    1. Store all nodes and assing themselves as representatives of tree
    2. When testing edge, find if both nodes in edge are in the same tree
    3. If they are then edge will create a cycle
"""


WeightedEdge = namedtuple('WeightedEdge', ['weight', 'node_from', 'node_to'])


def is_edge_create_cycle(reps, edge):
    _, node_a, node_b = edge
    reps_to_update = [node_a, node_b]

    rep_a = reps[node_a]

    # find root of tree which contain node_a
    while rep_a != reps[rep_a]:
        reps_to_update.append(rep_a)
        rep_a = reps[rep_a]

    rep_b = reps[node_b]

    # find root of tree which contain node_b
    while rep_b != reps[rep_b]:
        reps_to_update.append(rep_b)
        rep_b = reps[rep_b]

    if rep_a == rep_b:
        return True

    for rep in reps_to_update:
        reps[rep] = rep_a

    return False


def get_edges_from_graph(graph):
    visited = set()

    for node, children in graph.items():
        for child, weight in children.items():
            nodes = [node, child]
            nodes.sort()
            edge = WeightedEdge(weight, nodes[0], nodes[1])
            visited.add(edge)

    return list(visited)


def kruskal(graph):
    edges = get_edges_from_graph(graph)
    edges.sort(key=lambda x: x.weight)
    representatives = {}
    result = []

    for node in graph:
        representatives[node] = node

    for edge in edges:
        if not is_edge_create_cycle(representatives, edge):
            result.append(edge)

    return result


if __name__ == '__main__':
    graph = {
        'A': {
            'B': 2,
            'C': 3,
            'D': 3,
        },
        'B': {
            'A': 2,
            'C': 4,
            'E': 3,
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
            'C': 5,
            'F': 7,
        },
        'E': {
            'B': 3,
            'C': 1,
            'F': 8,
        },
        'F': {
            'C': 6,
            'D': 7,
            'E': 8,
            'G': 9,
        },
        'G': {
            'F': 9,
        },
    }

    result = get_edges_from_graph(graph)
    assert len(result) == len(set(result)), len(result)

    result = is_edge_create_cycle({'A': 'A', 'B': 'B'}, WeightedEdge(1, 'A', 'B'))
    assert result == False

    result = is_edge_create_cycle({'A': 'A', 'B': 'A'}, WeightedEdge(1, 'A', 'B'))
    assert result == True

    result = kruskal(graph)

    total_weight = 0

    for weight, _, _ in result:
        total_weight += weight

    assert total_weight == 24, total_weight
