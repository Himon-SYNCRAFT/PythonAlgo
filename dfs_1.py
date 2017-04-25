def dfs(graph, root, max_depth=100):
    """ Depth first search over a graph with max depth"""
    queue, visited = [(root, 0)], set()

    while queue:
        node, depth = queue.pop()

        if node not in visited:
            visited.add(node)
            yield node

            children = graph.get(node, [])

            if depth + 1 <= max_depth:
                for child in reversed(children):
                    queue.append((child, depth + 1))


if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6, 7],
        4: [2],
        5: [2],
        6: [3],
        7: [3],
    }

    result = list(dfs(graph, 1))
    assert result == [1, 2, 4, 5, 3, 6, 7], result

    result = list(dfs(graph, 1, 1))
    assert result == [1, 2, 3], result

    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['D', 'F', 'A'],
        'C': ['G', 'A'],
        'D': ['B'],
        'E': ['A', 'F'],
        'F': ['E', 'B'],
        'G': ['C'],
    }

    result = list(dfs(graph, 'A'))
    assert result == ['A', 'B', 'D', 'F', 'E', 'C', 'G'], result

    result = list(dfs(graph, 'A', 1))
    assert result == ['A', 'B', 'C', 'E'], result
