from collections import deque
import copy

def bfs(r, c):

    queue = deque()
    foot_prints = set()

    queue.append((r, c))
    foot_prints.add((r, c))

    foot_prints_aw = set()

    time = 0

    while queue:

        for i in range(len(active_water)):

            aw_r, aw_c = active_water.popleft()
            foot_prints_aw.add((aw_r, aw_c))

            for j in range(4):

                aw_ar = aw_r + dr[j]
                aw_ac = aw_c + dc[j]

                if 0 <= aw_ar < R and 0 <= aw_ac < C:
                    if matrix[aw_ar][aw_ac] != "D" and matrix[aw_ar][aw_ac] != "X" and (aw_ar, aw_ac) not in foot_prints_aw:

                        matrix[aw_ar][aw_ac] = "*"
                        active_water.append((aw_ar, aw_ac))
                        foot_prints_aw.add((aw_ar, aw_ac))


        for i in range(len(queue)):

            r, c = queue.popleft()

            if matrix[r][c] == "D":
                return time

            for i in range(4):

                ar = r + dr[i]
                ac = c + dc[i]

                if 0 <= ar < R and 0 <= ac < C:
                    if (ar, ac) not in foot_prints and matrix[ar][ac] != "*" and matrix[ar][ac] != "X":

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))

        time += 1

    return "KAKTUS"


R, C = map(int, input().split())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

matrix = [list(map(str, input().strip())) for _ in range(R)]

start_r = 0
start_c = 0

active_water = deque()

for i in range(R):
    for j in range(C):

        if matrix[i][j] == "S":

            matrix[i][j] = "."

            start_r = i
            start_c = j

        elif matrix[i][j] == "*":

            active_water.append((i, j))


print(bfs(start_r, start_c))

