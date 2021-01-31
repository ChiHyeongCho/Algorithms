
import math

v, e = map(int, input().split())

matrix = [[math.inf for j in range(v)] for i in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):

            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = math.inf

for i in range(v):

    if answer > matrix[i][i]:
        answer = matrix[i][i]

if answer == math.inf:
    print(-1)
else:
    print(answer)