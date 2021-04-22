
import math


def find(a):

    if a == parent[a]:
        return a

    else:
        parent[a] = find(parent[a])
        return parent[a]


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

link = [list(map(int, input().split())) for _ in range(n)]
alreadyLink = [list(map(int, input().split())) for _ in range(m)]
linkList = []

parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

answer = 0

for i in alreadyLink:

    x, y = i

    union(x, y)

for i in range(n):
    for j in range(i+1, n):

        xOne, yOne = link[i]
        xTwo, yTwo = link[j]

        distance = math.sqrt((xOne-xTwo)**2 + (yOne-yTwo)**2)

        linkList += [[i+1, j+1, distance]]

linkList.sort(key = lambda x : x[2])

for i in linkList:

    x, y, distance = i

    if find(x) == find(y):
        continue

    else:
        union(x, y)
        answer += distance

print(format(answer,".2f"))




