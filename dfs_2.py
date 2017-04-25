def traverse_preorder(graph, root):
    visited, queue = set(), [root]

    while queue:
        node = queue.pop()

        if node not in visited:
            visited.add(node)
            children = graph.get(node, [])
            queue.extend(reversed(children))
            yield node


def traverse_postorder(graph, root):
    visited, stack, result = set(), [root], []

    while stack:
        node = stack.pop()
        result.append(node)
        visited.add(node)
        children = graph.get(node, [])

        for child in children:
            if child not in visited:
                stack.append(child)

    result.reverse()
    return result


def map_graph(graph, root, fun, postorder=False):
    if not postorder:
        traverse = traverse_preorder
    else:
        traverse = traverse_postorder

    for item in traverse(graph, root):
        fun(item)



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

    result = list(traverse_preorder(graph, 1))
    assert result == [1, 2, 4, 5, 3, 6, 7]

    result = list(traverse_postorder(graph, 1))
    assert result == [4, 5, 2, 6, 7, 3, 1]

    map_graph(graph, root=1, fun=print)
