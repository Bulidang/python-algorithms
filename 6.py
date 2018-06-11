from random import randrange


# Tree class representation
class Node:
    lft = None
    rgt = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    return node


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif node.key > key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)


class Tree:
    root = None

    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)

    def __getitem__(self, key):
        return search(self.root, key)

    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True


# 6-3
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


# 6-4
def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


# 6-5
def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    lst = []
    while lft and rgt:
        if lft[-1] < rgt[-1]:
            lst.append(rgt.pop())
        else:
            lst.append(lft.pop())
    lst.reverse()
    return lft + rgt + lst


# seq = [randrange(10) for x in range(10)]
# print(seq, "\n", quicksort(seq), "\n", mergesort(seq))
