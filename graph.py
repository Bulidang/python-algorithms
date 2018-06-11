from pprint import pprint


# Listing 2-1 graph
a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}]

Ga = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

G5_7 = {
    'a': set('bc'),
    'b': set('dei'),
    'c': set('d'),
    'd': set('ah'),
    'e': set('f'),
    'f': set('g'),
    'g': set('eh'),
    'h': set('i'),
    'i': set('h')
}


# 《算法》P377的拓扑排序例子
G_top = {0: [5, 1, 6], 1: [], 2: [0, 3], 3: [5], 4: [], 5: [4], 6: [4, 9],
         7: [6], 8: [7], 9: [11, 12, 10], 10: [], 11: [12], 12: []}


# 《算法》P346的图4.1.18广度优先搜索
G_bfs = {0: [2, 1, 5], 1: [0, 2], 2: [0, 1, 3, 4], 3: [5, 4, 2], 4: [3, 2], 5: [3, 0]}


# input Graph
with open("tinyEWG.txt", 'r') as f:
    vertex_num = int(f.readline())
    G = {i: {} for i in range(vertex_num)}
    for line in f.readlines():
        date = line.split()
        if len(date) == 3:
            G[int(date[0])][int(date[1])] = float(date[2])
G_undirect = G
for u in G:
    for v in G[u]:
        G_undirect[v][u] = G[u][v]


# pprint(G)
