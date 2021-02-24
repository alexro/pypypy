from collections import deque

MAXV = 100
MAXDEGREE = 50

edges = [[0] * MAXDEGREE for _ in range(MAXV + 1)]
degree = [0] * (MAXV + 1)
nvertices = 0
nedges = 0


# for i, row in enumerate(edges):
#     print(i, row)


def add_edge(x, y, directed=False):
    global nedges
    edges[x][degree[x]] = y
    degree[x] += 1

    if not directed:
        add_edge(y, x, True)
    else:
        nedges += 1


def print_g():
    for v in range(1, nvertices + 1):
        print(v)
        for e in range(degree[v]):
            print(edges[v][e])
        print('-')


processed = [False] * (MAXV + 1)
discovered = [False] * (MAXV + 1)
parent = [0] * (MAXV + 1)


def process_vertex(v):
    print('vertex ', v)


def valid_edge(v, v2):
    print('valid ', v, v2)
    return True


def process_edge(v, v2):
    print('edge ', v, v2)


def bfs(start):
    q = deque()
    q.append(start)
    discovered[start] = True

    while q:
        v = q.popleft()
        process_vertex(v)
        for e in range(degree[v]):
            if valid_edge(v, edges[v][e]):
                if not discovered[edges[v][e]]:
                    q.append(edges[v][e])
                    discovered[edges[v][e]] = True
                    parent[edges[v][e]] = v
                if not processed[v]:
                    process_edge(v, edges[v][e])


finished = False


def dfs(v):
    if finished:
        return

    discovered[v] = True
    process_vertex(v)

    for e in range(degree[v]):
        v2 = edges[v][e]
        if valid_edge(v, v2):
            if not discovered[v2]:
                parent[v2] = v
                dfs(v2)
            elif not processed[v2]:
                process_edge(v, v2)

    if finished:
        return

    processed[v] = True


def find_path(v, v2):
    if v == v2 or v2 == 0:
        print(v)
    else:
        find_path(v, parent[v2])
        print(v2)


nvertices = 5
add_edge(1, 2)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 5)
add_edge(4, 1)

print_g()
dfs(1)
find_path(1, 5)
