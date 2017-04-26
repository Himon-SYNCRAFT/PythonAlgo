from collections import namedtuple
import pprint


pp = pprint.PrettyPrinter(indent=4)
WeightedEdge = namedtuple('WeightedEdge', ['node_from', 'node_to', 'weight'])


def find_union(edge, reprs):
    node_a = edge.node_from
    node_b = edge.node_to

    repr_a = reprs[node_a]
    len_a = 1

    repr_b = reprs[node_b]
    len_b = 1

    nodes_to_change = [node_a]

    while repr_a != reprs[repr_a]:
        nodes_to_change.append(repr_a)
        repr_a = reprs[repr_a]
        len_a += 1

    for node in nodes_to_change:
        reprs[node] = repr_a

    nodes_to_change = [node_b]
    while repr_b != reprs[repr_b]:
        nodes_to_change.append(repr_b)
        repr_b = reprs[repr_b]
        len_b += 1

    for node in nodes_to_change:
        reprs[node] = repr_b

    if repr_a != repr_b:
        if len_b <= len_a:
            reprs[repr_a] = repr_b
        else:
            reprs[repr_b] = repr_a

        return True

    return False


def kruskal(input_edges):
    edges = sorted(input_edges, key=lambda x: x.weight)
    nodes = set()

    for edge in edges:
        nodes.add(edge.node_from)
        nodes.add(edge.node_to)

    reprs = { node: node for node in nodes }
    result = []

    for edge in edges:
        add_edge = find_union(edge, reprs)

        if add_edge:
            result.append(edge)

    return result

if __name__ == '__main__':
    edges = [
        WeightedEdge(node_from='A', node_to='B', weight=1),
        WeightedEdge(node_from='A', node_to='D', weight=2),
        WeightedEdge(node_from='A', node_to='F', weight=2),
        WeightedEdge(node_from='B', node_to='C', weight=1),
        WeightedEdge(node_from='B', node_to='D', weight=2),
        WeightedEdge(node_from='C', node_to='E', weight=3),
        WeightedEdge(node_from='C', node_to='D', weight=1),
        WeightedEdge(node_from='D', node_to='E', weight=2),
        WeightedEdge(node_from='D', node_to='F', weight=1),
        WeightedEdge(node_from='D', node_to='G', weight=3),
        WeightedEdge(node_from='E', node_to='G', weight=1),
        WeightedEdge(node_from='F', node_to='G', weight=3),
    ]

    result = kruskal(edges)
    assert len(result) == 6, len(result)
