
import copy

N, L  = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

state = copy.deepcopy(matrix)

for i in range(N):
    state[i][0] = 0

print(state)

point = 0
time = 0
index = 0

while True:

    # state[i][0] == 1 이면 초록불

    if index < len(state) and point == matrix[index][0]:
        if state[index][0] == 1:

            point += 1
            index += 1
    else:

        point += 1

    if point == L+1:
        print(time)
        break

    time += 1

    # 신호등 상태 변환

    for i in range(index, len(state)):

        # 현상태 빨간불이면

        if state[i][0] == 0:

            state[i][1] -= 1

            if state[i][1] == 0:
                state[i][1] = matrix[i][1]
                state[i][0] = 1

        else:

            state[i][2] -= 1

            if state[i][2] == 0:
                state[i][2] = matrix[i][2]
                state[i][0] = 0



