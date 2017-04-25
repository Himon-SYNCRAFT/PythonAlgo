from random import sample, randint


def dag_generator(number_of_nodes=6):
    """
    Generating Directed Acyclic Graph as dict with connected nodes in set (only one edge between two nodes).
    Nodes are topologically sorted as indexes eg. node 1 have no dependencies and next nodes depends only on nodes
    that precedes them.
    """
    dag = {key: set() for key in range(1, number_of_nodes + 1)}

    for key in dag:
        population = range(key + 1, number_of_nodes + 1)

        k = randint(0, number_of_nodes - key)
        values = sample(population, k)
        dag[key] = set(values)

    return dag


if __name__ == '__main__':
    print(dag_generator())
