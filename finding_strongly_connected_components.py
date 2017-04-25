from collections import defaultdict


def topsort(graph):
    visited, result = set(), list()

    def recurse(node):
        if node in visited: return
        visited.add(node)

        for child in graph[node]:
            recurse(child)

        result.append(node)

    for node in graph:
        recurse(node)

    result.reverse()
    return result


def transpose_graph(graph):
    """ Reverse direction of edges in graph """
    result = dict()

    for node in graph:
        result[node] = set()

    for parent, children in graph.items():
        for child in children:
            result[child].add(parent)

    return result


def walk(graph, start, skip=set()):
    visited, queue = set(), set()
    queue.add(start)

    while queue:
        parent = queue.pop()
        print('w', parent)
        visited.add(parent)

        for child in graph[parent].difference(visited, skip):
            queue.add(child)

    return visited


def find_strongly_connected_components(graph):
    transposed_graph = transpose_graph(graph)
    components, visited = list(), set()
    print('t', topsort(graph))

    for item in topsort(graph):
        print('f', item)
        if item in visited: continue
        component = walk(transposed_graph, item, visited)
        print(component)
        visited.update(component)
        components.append(component)

    return components


if __name__ == '__main__':
    graph = {
        1: {2, 3},
        2: {4, 5},
        3: {6, 7},
        4: set(),
        5: set(),
        6: set(),
        7: set(),
    }

    result = transpose_graph(graph)
    assert result == {
        1: set(),
        2: {1},
        3: {1},
        4: {2},
        5: {2},
        6: {3},
        7: {3},
    }, result

    graph = {
        'a': set(['b', 'c']),
        'b': set(['d', 'e', 'i']),
        'c': set(['d']),
        'd': set(['a', 'h']),
        'e': set(['f']),
        'f': set(['g']),
        'g': set(['e', 'h']),
        'h': set(['i']),
        'i': set(['h']),
    }

    print('find_strongly_connected_components', find_strongly_connected_components(graph))
