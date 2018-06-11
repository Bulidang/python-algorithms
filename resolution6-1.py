import numpy as np


#(L, H, R)
lst = [[0, 2, 1],
       [0.5, 1.5, 3],
       [2, 3, 4],
       [5, 1, 7.5],
       [6, 2, 9],
       [6.5, 3, 8.5],
       [2.5, 2.5, 8]]
lst = np.array(lst)

print(lst[:, 0])

# a = [lst[i][0] for i in range(7)]
# print(a)


def merge_skyline(lst):
    mid = len(lst) // 2
    lft, rgt = lst[:mid], lst[mid:]
    if lft > 1:
        lft = merge_skyline(lft)
    if rgt > 1:
        rgt = merge_skyline(rgt)
    sky = []
    u = lft[-1][2]
    for i in rgt[:, 0]:
        if rgt[i, 0] < u:

    return sky
