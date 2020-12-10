def make(a):
    def aga(arg):
        a.append(arg)

    def ogo():
        print(a)

    return aga, ogo


aga1, ogo1 = make([])
aga2, ogo2 = make([])

aga1('kuku1')
aga2('kuku2')

ogo1()
ogo2()

aga1('kuku1')
aga2('kuku2')

ogo1()
ogo2()