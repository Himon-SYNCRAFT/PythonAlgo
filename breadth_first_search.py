from collections import deque


def breadth_first_search(graph, root):
    visited, queue = set(), deque([root])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            yield node

            children = graph.get(node, [])
            queue.extend(children)


def distances(graph, start):
    visited, queue, distances = set(), deque([start]), { start: 0 }

    while queue:
        node = queue.popleft()
        visited.add(node)

        distance = distances[node] + 1

        children = graph.get(node, [])

        for child in children:
            if child not in visited:
                queue.append(child)
                distances[child] = distance

    return distances




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

    result = list(breadth_first_search(graph, root=1))
    assert result == [1, 2, 3, 4, 5, 6, 7]

    result = distances(graph, start=1)
    assert result == { 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2 }

    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['D', 'F', 'A'],
        'C': ['G', 'A'],
        'D': ['B'],
        'E': ['A', 'F'],
        'F': ['E', 'B'],
        'G': ['C'],
    }

    result = list(breadth_first_search(graph, 'A'))
    assert result == ['A', 'B', 'C', 'E', 'D', 'F', 'G'], result

    result = distances(graph, start='A')
    assert result == { 'A': 0, 'B': 1, 'C': 1, 'E': 1, 'D': 2, 'F': 2, 'G': 2 }

    graph = {
        1: [2, 3],
        2: [4],
        3: [6],
        4: [5],
        5: [6],
        6: []
    }

    result = list(breadth_first_search(graph, root=1))
    assert result == [1, 2, 3, 4, 6, 5]

    result = distances(graph, start=1)
    assert result == { 1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 2 }
