from dag_generator import dag_generator

def naive_topsort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)

    v = S.pop()
    seq = naive_topsort(G, S)

    min_i = 0

    for index, value in enumerate(seq):
        if v in G[value]: min_i = index + 1

    seq.insert(min_i, v)
    return seq


if __name__ == '__main__':
    for i in range(10):
        G = dag_generator(number_of_nodes=6)
        sorted_list = naive_topsort(G)
        print(G, sorted_list)
        assert sorted_list == [1, 2, 3, 4, 5, 6], sorted_list
