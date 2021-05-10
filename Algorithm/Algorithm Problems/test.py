

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

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

for i in range(m):

    cal, a, b = map(int, input().split())

    if cal == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")

        else:
            print("NO")