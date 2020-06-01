
from collections import deque

def bfs(i, j):

    queue = deque()
    foot_prints = set()

    queue.append((i, j))
    foot_prints.add((i, j))

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = r + dr[k]
            ac = c + dc[k]

            if 0 <= ar < R and 0 <= ac < C:
                if matrix[ar][ac] == 0 and (ar, ac) not in foot_prints :

                    queue.append((ar, ac))
                    foot_prints.add((ar, ac))

                elif matrix[ar][ac] == 1 and (ar, ac) not in foot_prints:

                    remove.append((ar, ac))
                    foot_prints.add((ar, ac))


R, C = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(R)]

left_cheese = 0

dr = [1,0,-1,0]
dc = [0,1,0,-1]

time = 0

while True:

    remove = deque()
    bfs(0, 0)

    if len(remove) == 0:
        print(time)
        print(left_cheese)
        break

    left_cheese = len(remove)

    for i in range(len(remove)):

        a, b = remove.popleft()

        matrix[a][b] = 0

    time += 1