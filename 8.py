from graph import *
from itertools import combinations
from functools import wraps
from collections import defaultdict


# 8-1
def naive_lis(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
                # list(combinations('ABCD', 2)) -->AB AC AD BC BD CD
            if list(sub) == sorted(sub):
                return sub


# 8-2
def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


@memo
def C(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    return C(n - 1, k) + C(n - 1, k - 1)


def C_iter(n, k):
    C = defaultdict(int)
    for row in range(n + 1):
        C[row, 0] = 1
        for col in range(1, k + 1):
            C[row, col] = C[row - 1, col] + C[row - 1, col - 1]
    return C[n, k]


# 8-3
def dag_shortest_path(G, s, t):
    @memo
    def distance(u):
        if u == t:
            return 0
        return min(G[u][v] + distance(v) for v in G[u])
    return distance(s)


# print(C_iter(100, 50))
# print(naive_lis([3, 1, 0, 2, 4]))
print(dag_shortest_path(G, 0, 7))
