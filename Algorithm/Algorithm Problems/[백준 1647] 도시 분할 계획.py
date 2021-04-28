
import sys

n, m = map(int, sys.stdin.readline().split())

link = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 크루스칼 알고리즘

parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]


def find(x):

    if x == parent[x]:
        return x

    else:

        parent[x] = find(parent[x])

        return parent[x]


def union(a, b):

    x = find(a)
    y = find(b)

    if x == y:
        return

    elif rank[x] < rank[y]:
        parent[x] = y
        rank[y] += 1

    else:
        parent[y] = x
        rank[x] += 1

    return


link.sort(key = lambda x : x[2])

treeEdges = 0
mst = []
mstCost = 0

for i in range(m):
    if treeEdges == n-1:
        break

    u, v, wt = link[i]

    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, wt))
        mstCost += wt
        treeEdges += 1

maxLength = 0

for i in range(len(mst)):

    if maxLength < mst[i][2]:
        maxLength = mst[i][2]

print(mstCost-maxLength)