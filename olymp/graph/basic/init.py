def init(n):
    g = [[] for _ in range(n + 1)]
    return g


def add_edge(g, a, b, directed=False):
    g[a].append(b)
    if not directed:
        add_edge(g, b, a, True)


def print_graph(g):
    for k in range(len(g)):
        if len(g[k]) == 0:
            continue
        print(k)
        for e in g[k]:
            print(e, end=',')
        print('\n')


"""

g = init(100)
add_edge(g, 1, 2)
add_edge(g, 1, 3)
add_edge(g, 100, 3)

print_graph(g)

"""
