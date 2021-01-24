
from collections import deque

def bfs(i, j, color):

    #answerOne, answerTwo
    foot_prints[i][j] = 1
    queue = deque()
    queue.append((i, j))
    cnt = 0
    size = 0

    while queue:

        nr, nc = queue.popleft()
        new_matrix[nr][nc] = color
        size += 1

        for k in range(4):

            ar = nr + dr[k]
            ac = nc + dc[k]

            if direction[k] & matrix[nr][nc] != direction[k]:
                if 0 <= ar < r and 0 <= ac < c and foot_prints[ar][ac] != 1:

                    queue.append((ar, ac))
                    foot_prints[ar][ac] = 1


    return size


c, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
new_matrix = [[0]*c for _ in range(r)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
direction =[1, 2, 4, 8]

foot_prints = [[0]*c for _ in range(r)]

color = 0
size_ = []

answerOne = 0
answerTwo = 0
answerThree = 0

for i in range(r):
    for j in range(c):

        if foot_prints[i][j] != 1:

            returnOne = bfs(i, j, color)
            answerOne += 1
            answerTwo = max(returnOne, answerTwo)
            size_ += [returnOne]
            color += 1


for i in range(r):
    for j in range(c):
        for k in range(4):

            ar = i + dr[k]
            ac = j + dc[k]

            if 0 <= ar < r and 0 <= ac < c:
                if new_matrix[i][j] != new_matrix[ar][ac]:
                    answerThree = max(answerThree, size_[new_matrix[i][j]] + size_[new_matrix[ar][ac]])

print(answerOne)
print(answerTwo)
print(answerThree)
