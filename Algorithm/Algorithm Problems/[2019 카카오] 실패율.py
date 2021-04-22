def solution(N, stages):

    users = len(stages)
    maxStage = N+1

    matrix = [0]*(maxStage+1)
    totalMatrix = [0]*(maxStage+1)
    failMatrix = [0]*(maxStage+1)

    answer  = []

    answerMatrix = [[0]*2 for _ in range (N)]

    for i in stages:
        matrix[i] += 1

    for i in range(1, len(matrix)):
        totalMatrix[i] = matrix[i] + totalMatrix[i-1]

    for i in range(1, len(matrix)):

        if users - totalMatrix[i-1] != 0:
            failMatrix[i] = matrix[i] / (users - totalMatrix[i-1])

        else:
            failMatrix[i] = 0


    for i in range (N):

        answerMatrix[i][0] = i+1
        answerMatrix[i][1] = failMatrix[i+1]


    answerMatrix.sort(key = lambda x : x[1], reverse= True)


    for i in range(len(answerMatrix)):
        answer += [answerMatrix[i][0]]


    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(	4, [4, 4, 4, 4, 4]))