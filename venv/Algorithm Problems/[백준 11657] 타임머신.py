
import math

n, m = map(int, input().split())
matrix = []
bfmatrix = [math.inf for _ in range(n+1)]
bfmatrix[1] = 0
checkCycle = False

for _ in range(m):
    matrix += [list(map(int, input().split()))]

for i in range(n):
    for j in range(m):

        start = matrix[j][0]
        end = matrix[j][1]
        weight = matrix[j][2]

        if bfmatrix[start] != math.inf and bfmatrix[end] > bfmatrix[start] + weight:
            bfmatrix[end] = bfmatrix[start] + weight

            if i == n-1:
                checkCycle = True

if checkCycle == True:
    print(-1)

else:
    for i in range(2, n+1):
        if bfmatrix[i] == math.inf:
            print(-1)

        else:
            print(bfmatrix[i])


