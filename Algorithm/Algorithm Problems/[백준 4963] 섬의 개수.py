
from collections import deque

def bfs(i, j):

    queue.append((i, j))
    foot_prints.add((i, j))

    while queue:

        r, c = queue.popleft()

        for k in range(8):

            ar = r + dr[k]
            ac = c + dc[k]

            if 0 <= ar < R and 0 <= ac < C:
                if matrix[ar][ac] == 1 and (ar, ac) not in foot_prints:

                    queue.append((ar, ac))
                    foot_prints.add((ar, ac))

while True:

    C, R = map(int, input().split())

    if C == 0 and R == 0:
        break

    answer = 0

    matrix = [list(map(int, input().split())) for _ in range(R)]


    dr = [1, 0, -1, 0, 1, -1, 1, -1]
    dc = [0, 1, 0, -1, -1, 1, 1, -1]


    queue = deque()
    foot_prints = set()

    for i in range(R):
        for j in range(C):

            if matrix[i][j] == 1 and (i, j) not in foot_prints:
                bfs(i, j)
                answer += 1

    print(answer)

