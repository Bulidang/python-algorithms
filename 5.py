from graph import *
from collections import deque


# 5-1
def walk(G, s, S=set()):
    """Walking Through a Connected Component of a Graph Represented Using Adjacency Sets"""
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


# 5-5
def iter_dfs(G, s):
    """Iterative Depth-First Search"""
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u


# def dfs(G, s, d, f, S=None, t=0):
#     if S is None:
#         S = set()
#     d[s] = t
#     t += 1
#     S.add(s)
#     for u in G[s]:
#         if u in S:
#             continue
#         t = dfs(G, s, d, f, S, t)
#     f[s] = t
#     t += 1
#     return t


# 5-8
def dfs_topsort(G):
    """Topological Sorting Based on Depth-First Search"""
    S, res = set(), []

    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res


# 5-10
def bfs(G, s):
    """Breadth-First Search"""
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P


# 5-11
def scc(G):
    """Kosaraju's Algorithm for Finding Strongly Connected Components(scc)"""
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen:
            continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs


def tr(G):
    """Transpose (reverse edges of) G"""
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT


# print(dfs_topsort(G_top))
# print(bfs(G_bfs, 0))
# print(list(iter_dfs(N, 0)))
# pprint(scc(G5_7))
