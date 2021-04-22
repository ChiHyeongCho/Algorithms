
import math

def find(x):


    if x == parent[x]:
        return x

    else:

        parent[x] = find(parent[x])
        return parent[x]

#########################################

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

#########################################

def kruskal(matrix):

    minTotalDistance = 0
    minTree = []

    for i in range(len(matrix)):

        x, y, distance = matrix[i]

        if find(x) != find(y):
            union(x, y)
            minTotalDistance += distance
            minTree += [[x, y]]

    return minTree, minTotalDistance

#########################################

n = int(input())

matrix = [list(map(float, input().split())) for _ in range(n)]
pointDistanceMatrix = []

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):

        a, b = matrix[i]
        c, d = matrix[j]

        distance = math.sqrt((a-c)**2 + (b-d)**2)

        if i > j:
            pointDistanceMatrix += [[i, j, distance]]

pointDistanceMatrix = sorted(pointDistanceMatrix, key = lambda pointDistanceMatrix: pointDistanceMatrix[2])

minimunTree, minDistance = kruskal(pointDistanceMatrix)

print(round(minDistance, 2))