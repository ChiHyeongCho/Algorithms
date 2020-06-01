from collections import deque
import copy

def bfs(i, j, h):

    queue.append((i, j))
    foot_prints.add((i, j))

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = r + dr[k]
            ac = c + dc[k]

            if 0 <= ar < N and 0 <= ac < N:
                if matrix[ar][ac] > h and (ar, ac) not in foot_prints:

                    queue.append((ar, ac))
                    foot_prints.add((ar, ac))




N = int(input())

matrix = [list(map(int, input().split()) for _ in range(N)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

region_max = 0
region_answer = 0

for i in range(N):

    local_max = max(matrix[i][:])

    region_max = max(region_max, local_max)

for i in range(region_max+1):

    foot_prints = set()
    queue = deque()

    local_answer = 0

    for r in range(N):
        for c in range(N):

            if (r, c) not in foot_prints and matrix[r][c] > i:
                bfs(r, c, i)
                local_answer += 1

    if region_answer < local_answer:

        region_answer = local_answer

print(region_answer)
