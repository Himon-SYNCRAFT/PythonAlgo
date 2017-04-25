def balance_factor(tree):
    if not tree or len(tree[1]) == 0: return 0

    l_height = tree_height(tree, tree[1][0])
    r_height = 0

    if len(tree[1]) == 2:
        r_height = tree_height(tree, tree[1][1])

    return r_height - l_height

def tree_height(tree, start=1):
    if not tree: return 0
    height = 1

    if len(tree[start]) > 0:
        height += max(tree_height(tree, node) for node in tree[start])

    return height


if __name__ == '__main__':
    tree = {
        1: [2, 3],
        2: [],
        3: [4, 5],
        4: [],
        5: []
    }

    assert tree_height(tree) == 3, tree_height(tree)
    assert tree_height(tree, 2) == 1, tree_height(tree, 2)
    assert tree_height(tree, 3) == 2, tree_height(tree, 3)
    assert balance_factor(tree) == 1

    tree = {

    }

    assert tree_height(tree) == 0, tree_height(tree)
    assert balance_factor(tree) == 0

    tree = {
        1: []
    }

    assert tree_height(tree) == 1, tree_height(tree)
    assert balance_factor(tree) == 0

    tree = {
        1: [2],
        2: [],
    }

    assert tree_height(tree) == 2, tree_height(tree)
    assert balance_factor(tree) == -1
