
from collections import deque

def check():

    local_answer = 0

    for i in range(N):
        for j in range(N):

            local_answer_lr = 0
            local_answer_ud = 0

            queue = deque()
            queue.append((i, j))
            foot_prints = set()
            foot_prints.add((i, j))

            while queue:

                r, c = queue.popleft()
                local_answer_lr += 1

                for k in [1,3]:

                    ar = r + dr[k]
                    ac = c + dc[k]

                    if 0 <= ar <  N and 0 <= ac < N:

                        if matrix[r][c] == matrix[ar][ac] and (ar, ac) not in foot_prints:

                            queue.append((ar, ac))
                            foot_prints.add((ar, ac))

            #위아래
            queue = deque()
            queue.append((i, j))
            foot_prints = set()
            foot_prints.add((i, j))

            while queue:

                r, c = queue.popleft()
                local_answer_ud += 1

                for k in [0, 2]:

                    ar = r + dr[k]
                    ac = c + dc[k]

                    if 0 <= ar < N and 0 <= ac < N:
                        if matrix[r][c] == matrix[ar][ac] and (ar, ac) not in foot_prints:

                            queue.append((ar, ac))
                            foot_prints.add((ar, ac))


            if max(local_answer_ud, local_answer_lr) > local_answer:

                local_answer = max(local_answer_ud, local_answer_lr)

    return local_answer


N = int(input())

matrix = [list(map(str, input().strip())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

region = 0

for i in range(N):
    for j in range(N):

        for k in range(2):

            ar = i + dr[k]
            ac = j + dc[k]

            if 0 <= ar < N and 0 <= ac < N:

                if matrix[i][j] != matrix[ar][ac]:

                    matrix[i][j], matrix[ar][ac] = matrix[ar][ac], matrix[i][j]

                    local = check()

                    matrix[ar][ac], matrix[i][j] = matrix[i][j], matrix[ar][ac]

                    if local > region:

                        region = local

print(region)