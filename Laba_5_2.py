inf = float('Inf')
start = int(input("Введите начальный пункт: "))
f = int(input("Введите конечный пункт: "))

def dijkstra(G, s):
    n = len(G)

    Q = [(0, s)]
    x = 0
    d = [inf for i in range(n)]
    d[s] = 0
    while len(Q) != 0:
        (x, s) = Q.pop(0)

        for v in range(n):
            if d[v] > d[s] + G[s][v]:
                d[v] = d[s] + G[s][v]
                Q.append((d[v], v))
    return d


def getPath(f):
    global d
    n = len(G)

    path = [f]
    while f != start:
        for v in range(n):
            if d[v] == d[f] - G[f][v]:
                path.append(v)
                f = v
    return path[::-1]


a = open('Graph.txt', 'r')
G = []
for line in a:
    k = 0
    l = line.split()
    for i in l:
        if i == 'inf':
            l[k] = float(i)
            k += 1
        else:
            l[k] = int(i)
            k += 1
    G.append(l)
a.close()
d = dijkstra(G, start)
d = [int(i) for i in d]
print(d)
p = (getPath(f))
print(p)
i = len(p)-1
k = 0
distance = 0
while k < i:
    a = p[k]
    b = p[k+1]
    distance += G[a][b]
    k += 1
print(distance)