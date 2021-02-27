from graph.basic.init import *


def dfs(g, v):
    def _dfs(g, v, discovered, processed, parents):
        def process_edge(v, child):
            if parents[child] != v:
                print('CYCLE DETECTED: ', child, '<->', parents[child], 'AND', child, '<->', v)

        discovered[v] = True
        # process_vertex(v)
        for child in g[v]:
            if not discovered[child]:
                parents[child] = v
                _dfs(g, child, discovered, processed, parents)
            elif not processed[child]:
                process_edge(v, child)

        processed[v] = True

    def _start(g, v):
        discovered = [False] * len(g)
        processed = [False] * len(g)
        parents = [0] * len(g)
        _dfs(g, v, discovered, processed, parents)
        return parents

    return _start(g, v)


g = init(100)
add_edge(g, 1, 2)
add_edge(g, 1, 3)
add_edge(g, 100, 3)
add_edge(g, 2, 3)

p = dfs(g, 1)
print(p)
