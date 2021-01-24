
import math

n = int(input())
m = int(input())

matrix = []
floydMatrix = [[math.inf] * n for _ in range(n)]

for i in range(m):

    matrix += [list(map(int, input().split()))]
    floydMatrix[matrix[i][0]-1][matrix[i][1]-1] = min(matrix[i][2], floydMatrix[matrix[i][0]-1][matrix[i][1]-1])

for i in range(n):

    floydMatrix[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):

            if floydMatrix[j][k] > floydMatrix[j][i] + floydMatrix[i][k]:
                floydMatrix[j][k] = floydMatrix[j][i] + floydMatrix[i][k]

for i in range(n):
    for j in range(n):
        if floydMatrix[i][j] == math.inf:
            print(str(0), end = " ")
        else:
            print(str(floydMatrix[i][j]), end = " ")

    print()
