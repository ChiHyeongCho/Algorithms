
import math

n = int(input())

matrix = list(map(int, input().split()))
dpMatrix = [0 for _ in range(n)]
dpMatrix[0] = matrix[0]

answer = dpMatrix[0]

for i in range(1, n):
    dpMatrix[i] = max(dpMatrix[i-1] + matrix[i], matrix[i])
    answer = max(answer, dpMatrix[i])

print(answer)


    



