from itertools import permutations
import copy

def turn(r, c, s):

    for i in range(1, s+1):

        start = matrix[r-i][c-i]

        for j in range(0, i*2):

            matrix[r-i+j][c-i] = matrix[r-i+j+1][c-i]

        for j in range(0, i*2):

            matrix[r+i][c-i+j] = matrix[r+i][c-i+j+1]

        for j in range(0, i*2):

            matrix[r+i-j][c+i] = matrix[r+i-j-1][c+i]

        for j in range(0, i*2):

            matrix[r-i][c+i-j] = matrix[r-i][c+i-j-1]

        matrix[r-i][c-i+1] = start

    return

def find_answer(answer):

    region = answer

    for i in range(N):

        local = sum(matrix[i])

        if local < region:

            region = local

    return region

N, M, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
back_up = copy.deepcopy(matrix)

order = [list(map(int, input().split())) for _ in range(K)]
permu_order = list(permutations(order, K))

answer = 1000*1000

for k in range(len(permu_order)):

    matrix = copy.deepcopy(back_up)

    for i in permu_order[k]:

        r, c, s = i

        turn(r-1, c-1, s)

    local_answer = find_answer(answer)

    if local_answer < answer:

        answer = local_answer

print(answer)