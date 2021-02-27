from collections import deque
from graph.basic.init import *


def bfs(g, v, process_vertex, process_edge):
    discovered = [False] * len(g)
    processed = [False] * len(g)
    parents = [0] * len(g)

    queue = deque()
    queue.append(v)
    discovered[v] = True

    while queue:
        v = queue.popleft()
        process_vertex(v)
        processed[v] = True

        for child in g[v]:
            if not discovered[child]:
                queue.append(child)
                discovered[child] = True
                parents[child] = v
            if not processed[child]:
                process_edge(v, child)
    print(parents)
    return parents


def print_parents(p, v):
    if v == 0:
        print(0)
        return
    print(v, end='<-')
    print_parents(p, p[v])


g = init(100)
add_edge(g, 1, 2)
add_edge(g, 1, 3)
add_edge(g, 100, 3)

print_graph(g)


def p_v(v):
    print('v: ', v)


def p_e(v, child):
    print('v-e: ', v, child)


p = bfs(g, 1, p_v, p_e)
print_parents(p, 100)
