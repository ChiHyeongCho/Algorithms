from collections import deque


def solution(N, simulation_data):
    answer = 0

    # 문제풀이 데이터 생성

    desk = [0]*N
    for i in range(N):
        desk[i] = deque()
    line = deque()
    time = 0
    index = 0

    while True:

        if index == len(simulation_data) and len(line) == 0:
            break


        for i in range(len(desk)):

            if len(desk[i]) > 0:

                desk[i][0][1] -= 1

                if desk[i][0][1] == 0:
                    desk[i].popleft()

        if index != len(simulation_data):
            if simulation_data[index][0] == time:
                line.append(simulation_data[index])
                index += 1


        for i in range(len(desk)):
            if len(desk[i]) == 0 and len(line) > 0:
                customer = line.popleft()
                desk[i].append(customer)

        if len(line) > 0:
            answer += len(line)

        time += 1

    return answer


print(solution(2, [[0, 3], [2, 5], [4, 2], [5, 3]]))