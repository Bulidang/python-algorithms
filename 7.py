from graph import *
from heapq import heapify, heappush, heappop
from itertools import count


# 7-1 & 7-2
def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)  # convert list to heap
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))
    return trees[0][-1]


def codes(tree, prefix=""):
    """Extracting Huffman Codes from a Huffman Tree"""
    if len(tree) == 1:
        yield (tree, prefix)
        return
    for bit, child in zip("01", tree):
        for pair in codes(child, prefix + bit):
            yield pair


# seq = "abcdefghi"
# frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
# trees = huffman(seq, frq)
# print(trees)
# print(list(codes(trees)))


# 7-3
def naive_kruskal(G):
    E = [(G[u][v], u, v)for u in G for v in G[u]]
    T = set()
    C = {u: u for u in G}

    def naive_find(C, u):
        while C[u] != u:
            u = C[u]
        return u

    def naive_union(C, u, v):
        u = naive_find(C, u)
        v = naive_find(C, v)
        C[u] = v

    for _, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)
    return T


# 7-4
def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}

    def find(C, u):
        if C[u] != u:
            C[u] = find(C, C[u])  # path compression
        return C[u]

    def union(C, R, u, v):
        u, v = find(C, u), find(C, v)
        if R[u] > R[v]:
            C[v] = u
        else:
            C[u] = v
        if R[u] == R[v]:
            R[v] += 1

    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


# 7-5
def prim(G, s):
    Presence, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in Presence:
            continue
        Presence[u] = p
        for v, weight in G[u].items():
            heappush(Q, (weight, u, v))
    return Presence


# pprint(G)
# print("naive_kruskal: %s" % naive_kruskal(G))
# print("kruskal:       %s" % kruskal(G))
# print("prim:          %s" % prim(G_undirect, 0))
