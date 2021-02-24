def dfs(g, v, visited, ticks):
    if v in visited:
        return
    ticks[0] += 1
    print('in: ', v, ticks[0])
    visited.add(v)
    for n in g[v]:
        dfs(g, n, visited, ticks)
    print('out: ', v, ticks[0])
    ticks[0] += 1


def bfs(a):
    visited = set()
    nodes = {1}
    nodes2 = set()
    links = {}
    while nodes:
        for node in nodes:
            if node in visited:
                continue
            visited.add(node)

            links[node] = set()
            for v in range(1, len(a[node])):
                edge = a[node][v]
                if edge == 1:
                    nodes2.add(v)
                    links[node].add(v)

        nodes = nodes2
        nodes2 = set()

    print(visited)
    print(links)

    dfs(links, 1, set(), [0])


def test():
    a0 = [0, 0, 0, 0, 0]
    a1 = [0, 0, 1, 0, 0]
    a2 = [0, 1, 0, 1, 0]
    a3 = [0, 0, 1, 0, 1]
    a4 = [0, 0, 0, 1, 0]
    a = [a0, a1, a2, a3, a4]
    for row in a:
        print(row)
    bfs(a)


test()
