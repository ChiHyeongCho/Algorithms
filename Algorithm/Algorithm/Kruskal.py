
graph = [(1, 2, 13), (1, 3, 5), (2, 5, 9), (3, 4, 15), (3, 5, 3), (4, 5, 1), (4, 6, 7), (5, 6, 2)]
graph.sort(key = lambda x:x[2])

n = 6

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

treeEdges = 0
mst = []
mstCost = 0

for i in range(len(graph)):
    if treeEdges == n-1:
        break

    u, v, wt = graph[i]

    if find(u) != find(v):
        union(u, v)
        mst.append((u, v))
        mstCost += wt
        treeEdges += 1

print(mst)
print(mstCost)