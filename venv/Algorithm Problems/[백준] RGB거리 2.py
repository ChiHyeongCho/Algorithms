import math

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = math.inf

for k in range(3):

    dpMatrix = [[0] * 3 for _ in range(n)]

    for i in range(3):

        if i == k:
            dpMatrix[0][i] = matrix[0][i]

        else:
            dpMatrix[0][i] = math.inf

    for i in range(n-1):

        dpMatrix[i+1][0] = min(dpMatrix[i][1], dpMatrix[i][2]) + matrix[i+1][0]
        dpMatrix[i+1][1] = min(dpMatrix[i][0], dpMatrix[i][2]) + matrix[i+1][1]
        dpMatrix[i+1][2] = min(dpMatrix[i][0], dpMatrix[i][1]) + matrix[i+1][2]


    for i in range(3):
        if i == k:
            continue
        else:
            answer = min(dpMatrix[n-1][i], answer)


print(answer)