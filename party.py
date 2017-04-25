"""
Let's say you're going to invite some people to a party. You're considering n friends, but you know
that they will have a good time only if each of them know at least k others at the party. Solve
your problem by designing an algorithm for finding the largest possible subset of your friends
where everyone knows at least k of the others, if such a subset exist.
"""

from copy import deepcopy



def party(graph, k):
    graph = deepcopy(graph)
    vertices_to_remove = set(vertex for vertex, friends in graph.items() if len(friends) < k)
    count = 0

    while vertices_to_remove:
        vertex = vertices_to_remove.pop()
        friends = graph[vertex]
        del graph[vertex]

        for v in friends:
            count += 1
            graph[v].discard(vertex)

            if len(graph[v]) < k:
                vertices_to_remove.add(v)

    print(count)
    return list(graph.keys())

if __name__ == '__main__':
    graph = {
        1: set([2, 3, 5]),
        2: set([1, 3]),
        3: set([1, 2, 4, 5]),
        4: set([3, 5]),
        5: set([1, 3, 4])
    }

    assert party(graph, 3) == []
    assert len(party(graph, 2)) == 5

    graph = {
        1: set([2, 3, 4, 5, 6]),
        2: set([1, 3, 4, 5, 6]),
        3: set([1, 2, 4, 5, 6]),
        4: set([1, 2, 3, 5, 6]),
        5: set([1, 2, 3, 4, 6]),
        6: set([1, 2, 3, 4, 5]),
    }

    assert party(graph, 8) == []
