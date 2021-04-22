
from collections import deque


def bfs():

    global left_tomato

    for i in range(h):
        for j in range(r):
            for k in range(c):

                if matrix[i][j][k] == 1:
                    queue.append((i,j,k))
                    foot_prints.add((i,j,k))
                    left_tomato += 1

                elif matrix[i][j][k] == 0:
                    left_tomato += 1

    time = -1

    while queue:

        for i in range(len(queue)):

            x, y, z = queue.popleft()
            left_tomato -= 1

            for j in range(6):

                ax = x + dr[j]
                ay = y + dc[j]
                ah = z + dh[j]

                if 0 <= ax < h and 0 <= ay < r and 0 <= ah < c:
                    if matrix[ax][ay][ah] == 0 and (ax, ay, ah) not in foot_prints:
                        matrix[ax][ay][ah] = 1
                        queue.append((ax, ay, ah))
                        foot_prints.add((ax, ay, ah))

        time += 1

    return time

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

c, r, h  = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(r)] for _ in range(h)]

queue = deque()
foot_prints = set()
left_tomato = 0

T = bfs()


if left_tomato > 0:
    print(-1)
else:
    print(T)