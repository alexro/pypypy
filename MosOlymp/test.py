g = {
    1: {
        2: {
            3: None,
            4: None
        },
        5: None
    }
}


def walk(g):
    if g is None:
        return

    for key in g:
        walk(g[key])
        print(key)


walk(g)
