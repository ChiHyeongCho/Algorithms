
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix.sort(key = lambda x : x[0])

answer = 0

i = 0

while True:

    #print(i)

    if i == n-1:
        answer += matrix[i][1]
        break

    localAnswer = 0
    localState = True
    localMax = [0, 0]

    for j in range(i + 1, len(matrix)):

        if matrix[i][1] < matrix[j][1]:
            localAnswer = matrix[i][1] * (matrix[j][0] - matrix[i][0])
            i = j
            localState = False
            break

        if matrix[j][1] >= localMax[1]:
            localMax = [j, matrix[j][1]]

    if not localState:
        answer += localAnswer

    else:
        #print(matrix[i], matrix[localMax[0]][0] - matrix[i][0] )
        answer += matrix[i][1] + (matrix[localMax[0]][0] - matrix[i][0]-1) * localMax[1]
        i = localMax[0]

#    print(answer)


print(answer)