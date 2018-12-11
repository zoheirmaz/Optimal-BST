from functions import tree, summ

n = int(input('Enter n: '))

keys = []
# freq = []

for i in range(n):
    key = int(input('Enter key: '))
    freq = float(input('Enter freq: '))

    keys.append((key,freq))

keys.sort()

R = [[0 for x in range(n + 1)] for y in range(n + 1)]

A = [[0 for x in range(n + 1)] for y in range(n + 1)]

for i in range(n):
    A[i][i - 1] = 0
    A[i][i] = keys[i][1]
    R[i][i] = i
    R[i][i - 1] = 0

# ------------------------------------------

for diagonal in range(n):

    for i in range(n - diagonal):

        j = i + diagonal

        if i < j:

            min_list = []
            for k in range(i, j + 1):
                min_list.append(((A[i][k - 1] + A[k + 1][j]), k))

            # pprint(min_list)
            min_list.sort()

            A[i][j] = min_list[0][0] + summ(keys, i, j)

            # R[i][j] = a value of k that gave the minimum;
            R[i][j] = min_list[0][1]

# pprint(A)
# print()
# pprint(R)

print(tree(keys, R, 0, n - 1))
print()
print('Cost of Optimal binary search is ' + str(A[0][n - 1]))
