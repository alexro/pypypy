def walk(d, root):
    if root is None:
        keys = d.keys()
        for key in keys:
            walk(d, key)
    else:
        if d[root] is None:
            print(root)
            return

        keys = d[root].keys()
        for key in keys:
            print(root)
            walk(d[root], key)


def solve(d):
    walk(d, None)


def test():
    d = {
        'A': {
            'B': {
                'D': None
            },
            'C': {
                'F': {
                    'G': None
                }
            }
        }
    }
    solve(d)


test()
