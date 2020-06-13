
from collections import deque

def bfs_A(i, j):

    visited_A[i][j] = 1
    queue.append((i, j))

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = dr[k] + r
            ac = dc[k] + c

            if 0 <= ar < N and 0<= ac < N:
                if matrix[i][j] == matrix[ar][ac] and visited_A[ar][ac] == 0:

                    queue.append((ar, ac))
                    visited_A[ar][ac] = 1

def bfs_B(i, j):

    visited_B[i][j] = 1
    queue.append((i, j))

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = dr[k] + r
            ac = dc[k] + c

            if 0 <= ar < N and 0<= ac < N:
                if matrix[i][j] == "R" and matrix[ar][ac] != "B" and visited_B[ar][ac] == 0:

                    queue.append((ar, ac))
                    visited_B[ar][ac] = 1

                elif matrix[i][j] == "G" and matrix[ar][ac] != "B" and visited_B[ar][ac] == 0:

                    queue.append((ar, ac))
                    visited_B[ar][ac] = 1

                elif matrix[i][j] == "B" and matrix[ar][ac] == "B" and visited_B[ar][ac] == 0:

                    queue.append((ar, ac))
                    visited_B[ar][ac] = 1

N = int(input())

matrix = [list(map(str, input().strip())) for _ in range(N)]
visited_A = [[0]*N for _ in range(N)]
visited_B = [[0]*N for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

region_A = 0
region_B = 0

for i in range(N):
    for j in range(N):

        if visited_A[i][j] == 0:
            queue = deque()
            bfs_A(i, j)
            region_A += 1

        if visited_B[i][j] == 0:
            queue = deque()
            bfs_B(i, j)
            region_B += 1

print(region_A, region_B)