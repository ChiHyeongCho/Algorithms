from collections import deque

def bfs_x(r, c):

    queue = deque()
    foot_prints = set()

    queue.append((r, c))
    foot_prints.add((r, c))

    local = -1

    while queue:

        for j in range(len(queue)):

            xr, xc = queue.popleft()

            if matrix[xr][xc] != 0 and matrix[xr][xc] != matrix[r][c]:
                return local

            for i in range(4):

                ar = xr + dr[i]
                ac = xc + dc[i]

                if 0 <= ar < N and 0 <= ac < N:
                    if matrix[ar][ac] != matrix[r][c] and (ar, ac) not in foot_prints:

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))


        local += 1

    return 200

def bfs(r, c, number, foot_prints):

    queue = deque()
    queue.append((r, c))

    while queue:

        xr, xc = queue.popleft()

        for i in range(4):

            ar = xr + dr[i]
            ac = xc + dc[i]

            if 0 <= ar < N and 0 <= ac < N:

                if matrix[ar][ac] == 1 and (ar, ac) not in foot_prints:

                    matrix[ar][ac] = number
                    queue.append((ar, ac))
                    foot_prints.add((ar, ac))

    return


def split_region():

    foot_prints = set()
    number = 1

    for i in range(N):
        for j in range(N):

            if matrix[i][j] == 1 and (i, j) not in foot_prints:

                foot_prints.add((i, j))
                bfs(i, j, number, foot_prints)
                matrix[i][j] = number
                number += 1

    return

def find_min():

    region = 200

    for i in range(N):
        for j in range(N):

            if matrix[i][j] != 0:

                local = bfs_x(i, j)

                if local < region:
                    region = local

    return region

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

split_region()

print(find_min())
