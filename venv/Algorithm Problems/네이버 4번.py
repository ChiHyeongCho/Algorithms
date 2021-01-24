
def simulation(maze, person, dr, dc):

    answer = 0


    while True:

        if person[1] == len(maze)-1 and person[2] == len(maze)-1:
            break

        # 왼편에 벽이 있을 경우

        wallState = False

        if person[0] == 0:

            wr = person[1]
            wc = person[2] - 1

            if wc == -1:
                wallState = True

            elif wc != -1 and maze[wr][wc] == 1:
                wallState = True

        if person[0] == 1:

            wr = person[1] - 1
            wc = person[2]

            if wr == -1:
                wallState = True

            elif wr != -1 and maze[wr][wc] == 1:
                wallState = True

        if person[0] == 2:

            wr = person[1]
            wc = person[2] + 1

            if wc == len(maze):
                wallState = True

            elif wc != len(maze) and maze[wr][wc] == 1:
                wallState = True

        if person[0] == 3:

            wr = person[1] + 1
            wc = person[2]

            if wr == len(maze):
                wallState = True

            elif wr != len(maze) and maze[wr][wc] == 1:
                wallState = True

        #print(person, wallState)

        ar = person[1] + dr[person[0]]
        ac = person[2] + dc[person[0]]

        # 왼편에 벽이 있을 때

        if wallState == True:

            # 앞에 갈 수 있는 경우 (장애물이 없을 때)

            if 0 <= ar < len(maze) and 0 <= ac < len(maze) and maze[ar][ac] != 1:

                person[1] = ar
                person[2] = ac

            # 앞에 갈 수 없는 경우 회전 필요 (장애물이 있을 경우)

            else:

                for i in range(4):

                    ar = person[1] + dr[i]
                    ac = person[2] + dc[i]

                    if 0 <= ar < len(maze) and 0<= ac < len(maze) and maze[ar][ac] != 1:
                        person[0] = i
                        person[1] = ar
                        person[2] = ac

                        break

        # 왼편에 벽이 없을 때

        else:

            person[0] = person[0] - 1

            if person[0] == -1:
                person[0] = 3

            person[1] += dr[person[0]]
            person[2] += dc[person[0]]

        answer += 1

    return answer


def solution(maze):

    # 방향 및 위치 (0 : 북, 1 : 동, 2 : 남, 3 : 서)
    person = [0, 0, 0]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    # 초기 방향 설정

    if maze[1][0] == 1:
        person[0] = 1

    else:
        person[0] = 2


    answer = simulation(maze, person, dr, dc)

    return answer


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))