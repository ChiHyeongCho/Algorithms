
from itertools import combinations
from collections import deque


def bfs():

    time = -1
    deter = 0

    while queue:

        for i in range(len(queue)):

            r, c = queue.popleft()

            if matrix[r][c] == 0:

                deter += 1

            if deter == blank:
                return time+1

            for j in range(4):

                ar = r + dr[j]
                ac = c + dc[j]

                if 0 <= ar < N and 0 <= ac < N:
                    if (ar, ac) not in foot_prints and matrix[ar][ac] != 1:

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))

        time += 1

    return -1



N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

virus = []
blank = 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):

        if matrix[i][j] == 2:

            virus += [(i,j)]

        elif matrix[i][j] == 0:

            blank += 1

combination_virus = list(combinations(virus, M))

region = 50*50

for i in range(len(combination_virus)):

    queue = deque()
    foot_prints = set()

    for j in range(len(combination_virus[i])):
        queue.append(combination_virus[i][j])
        foot_prints.add(combination_virus[i][j])

    local = bfs()

    if local != -1 and local < region:
        region = local

if region == 50*50:
    print(-1)
else:
    print(region)

