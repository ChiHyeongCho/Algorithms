
def dfs(current):

    footPrints.add(current)

    dpMatrix[current][0] = 1
    dpMatrix[current][1] = 0

    for i in tree[current]:

        if i not in footPrints:
            dfs(i)
            dpMatrix[current][0] += dpMatrix[i][1]
            dpMatrix[current][1] += max(dpMatrix[i][0], dpMatrix[i][1])

n = int(input())

tree = [[] for _ in range(n+1)]
footPrints = set()

for _ in range(n-1):

    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)


dpMatrix = [[0,0] for _ in range(n+1)]

dfs(1)

print(n - max(dpMatrix[1][0], dpMatrix[1][1]))