

N, H = map(int, input().split())


matrix_A = [0] * 500001
matrix_B = [0] * 500001

upMax = 0
downMax = 0

up = [0] * 500001
down = [0] * 500001
total = [0] * 500001

answerMin = 200000
answerNuM = 1

for i in range(N):

    if i % 2 == 0:

        k = int(input())

        matrix_A[k] += 1

        if k > upMax:
            upMax = k

    else:

        k = int(input())

        matrix_B[H-k+1] += 1

        if k < downMax:
            downMax = k

up[upMax] = matrix_A[upMax]
down[downMax] = matrix_B[downMax]

for i in range(upMax, 1, -1):

    up[i-1] += matrix_A[i-1] + up[i]

for i in range(downMax, H):

    down[i+1] += matrix_B[i+1] + down[i]



for i in range(1, H+1):

    total[i] = up[i] + down[i]

    if total[i] < answerMin:

        answerMin = total[i]
        answerNuM = 1

    elif total[i] == answerMin:

        answerNuM += 1

print(answerMin, answerNuM)