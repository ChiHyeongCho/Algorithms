
from collections import deque


def bfs(i, j, number):

    queue = deque()
    queue.append((i, j))
    foot_prints.add((i, j))
    matrix[i][j] = number

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = r + dr[k]
            ac = c + dc[k]

            if 0 <= ar < R and 0 <= ac < C:
                if matrix[ar][ac] == 1 and (ar, ac) not in foot_prints:

                    matrix[ar][ac] = number
                    foot_prints.add((ar, ac))
                    queue.append((ar, ac))


def find_A(i, j):

    queue = deque()
    foot_prints = set()

    queue.append((i, j))
    foot_prints.add((i, j))

    dist = 0

    while queue:

        for _ in range(len(queue)):

            r, c = queue.popleft()

            for k in range(2):

                ar = r + dr[k]
                ac = c + dc[k]

                if 0 <= ar < R and 0 <= ac < C:
                    if matrix[ar][ac] == 0 and (ar, ac) not in foot_prints:

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))

                    elif matrix[ar][ac] != 0 and matrix[ar][ac] != matrix[i][j] and dist > 1:

                        if node[matrix[ar][ac]-1][matrix[i][j]-1] > dist:

                            node[matrix[ar][ac]-1][matrix[i][j]-1] = dist
        dist += 1

def find_B(i, j):

    queue = deque()
    foot_prints = set()

    queue.append((i, j))
    foot_prints.add((i, j))

    dist = 0

    while queue:

        for _ in range(len(queue)):

            r, c = queue.popleft()

            for k in range(2, 4):

                ar = r + dr[k]
                ac = c + dc[k]

                if 0 <= ar < R and 0 <= ac < C:
                    if matrix[ar][ac] == 0 and (ar, ac) not in foot_prints:

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))

                    elif matrix[ar][ac] != 0 and matrix[ar][ac] != matrix[i][j] and dist > 1:

                        if node[matrix[ar][ac]-1][matrix[i][j]-1] > dist:

                            node[matrix[ar][ac]-1][matrix[i][j]-1] = dist
        dist += 1


R, C = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(R)]

foot_prints = set()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

number = 0

for i in range(R):
    for j in range(C):

        if matrix[i][j] == 1 and (i, j) not in foot_prints:

            number += 1
            bfs(i, j, number)

node = [[1000]*number for _ in range(number)]

for i in range(R):
    for j in range(C):

        if matrix[i][j] != 0:

            find_A(i, j)
            find_B(i, j)

edge = []

for i in range(number):
    for j in range(i, number):

        if node[i][j] != 1000:

            edge += [[i, j, node[i][j]]]

edge.sort(key = lambda x:x[2])
cost = 0

parent = [0]*number
level = [1]*number

for i in range(number):

    parent[i] = i

def find(i):

    if (i == parent[i]):
        return i

    parent[i] = find(parent[i])

    return parent[i]

def union(i, j, c):

    i = find(i)
    j = find(j)

    if i == j:
        return

    if level[i] > level[j]:

        level[j] += level[i]
        parent[i] = j

    else:

        level[i] += level[j]
        parent[j] = i

    global cost

    cost += c

    return

for i in edge:

    union(i[0], i[1], i[2])



if max(level) != number:
    print(-1)

else:
    print(cost)
