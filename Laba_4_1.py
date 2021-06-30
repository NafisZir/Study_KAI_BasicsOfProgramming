def read_graph(m, n):
    G = [[0 for k in range(m)]for j in range(m)]
    for k in range(n):
        a, b = input("Введите смежные вершины: ").split()
        a = int(a)
        b = int(b)
        add_edge(G, a, b)
        add_edge(G, b, a)
    return G


def add_edge(G, a, b):
    G[a].pop(b)
    G[a].insert(b, 1)


def seal_matrix(G):
    print()
    for k in range(m):
        print(" ", k, end="")
    print()
    i = 0
    while i < m:
        print(i, G[i])
        i += 1


def task_a_g(G, m):
    seal_matrix(G)
    i, a, g = 0, 0, 0
    while i < m:
        j = 0
        k = 0
        while j < m:
            if i == j and G[i][j] == 1:
                a += 1
                j += 1
                continue
            if G[i][j] == 1:
                k += 1
            if k == m - 1:
                g += 1
            j += 1
        i += 1
    if a > 0:
        print("В графе есть петли.")
    else:
        print("В графе нет петель.")

    if g > 0:
        print("В графе есть вершина смежная со всеми.")
    else:
        print("В графе нет вершин, смежных со всеми.")


def task_b(G, m):
    seal_matrix(G)
    i, b = 0, 0
    while i < m:
        j = 0
        while j < m:
            if G[i][j] == 1:
                break
            if j == m - 1:
                b += 1
                i = m - 1
            j += 1
        i += 1
    if b > 0:
        print("В графе есть несмежные вершины.")
    else:
        print("В графе все вершины смежные.")


def task_v(G, m):
    i, q = 0, 0
    while i < m:
        j = 0
        while j < m:
            if G[i][j] == 1:
                print("Вершина", i, "смежен с вершиной", j)
            j += 1
        print()
        i += 1


def task_d_e_j(G, m):
    lst = []
    lst2 = []
    for i in range(m):
        s = 0
        for j in range(m):
            s = s + G[i][j]
        print("Степень вершины ", i, " равен ", s)
        lst.append(s)
        if s == 1:
            lst2.append(i)
    print("Номера вершин со степенью 1: ", lst2, "\nСтепень графа равен: ", max(lst))


i = 0
while i < 1:
    m = int(input("Введите количество вершин: "))
    if m < 0 or m > 11:
        print("Неправильный ввод")
        continue
    i += 1
i = 0
while i < 1:
    n = int(input("Введите количество рёбер: "))
    if n < 0:
        print("Неправильный ввод")
        continue
    i += 1


G = read_graph(m, n)
task_a_g(G, m)
task_b(G, m)
task_v(G, m)
task_d_e_j(G, m)

