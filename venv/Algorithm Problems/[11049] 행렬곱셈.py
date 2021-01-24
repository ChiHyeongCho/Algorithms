

n = int(input())
matrix = []
globalMax = 0;

# 앞 지금까지 최소 // 뒤 뒤에서부터 계산값
dpMatrix = list([0]*n for _ in range(n))

for i in range(n):

    matrix += [list(map(int, input().split()))]
    dpMatrix[i][i] = 0

for i in range(n-1):

    dpMatrix[i][i+1] = matrix[i][0]*matrix[i][1]*matrix[i+1][1]

for i in range(n-2, 0, -1):
    for j in range(n-i, n):

        dpMatrix[j-2][j] = 2**32
        print(dpMatrix)

for i in range(n-2, 0, -1):
    for j in range(n-i, n):

        dpMatrix[j-2][j] = 2**32

        for k in range(n-i):

            print(j-k)
            dpMatrix[j][j+1] = min(dpMatrix[j][j+1], dpMatrix[j-k][j+1] + dpMatrix[j][j+1+k+1] + matrix[j-k][0]*matrix[j-k][1]*matrix[j][1])
            print(dpMatrix)

print(dpMatrix)





