from binarytree import Node


def tree(keys, k, i, j):
    r = k[i][j]

    if i == j:
        root = Node(keys[r][0])

    else:
        root = Node(keys[r][0])
        if i <= r - 1:
            root.left = tree(keys, k, i, r - 1)
        if r + 1 <= j:
            root.right = tree(keys, k, r + 1, j)

    return root


def summ(P, I, J):
    sum_p = 0
    for m in range(I, J + 1):
        sum_p += P[m][1]
    return sum_p
