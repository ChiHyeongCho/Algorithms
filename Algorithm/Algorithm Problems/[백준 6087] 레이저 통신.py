
import math
from queue import PriorityQueue

def bfs(lasers):

    queue = PriorityQueue()
    queue.put((0, (lasers[0][0]-1, lasers[0][1], 0)))
    queue.put((0, (lasers[0][0], lasers[0][1]+1, 1)))
    queue.put((0, (lasers[0][0]+1, lasers[0][1], 2)))
    queue.put((0, (lasers[0][0], lasers[0][1]-1, 3)))

    footPrints = set()

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while queue:

        answerNow, (rNow, cNow, dNow) = queue.get()

        #print(answerNow)

        if rNow < 0 or cNow < 0 or rNow >= r or cNow >= c:
            continue

        if matrix[rNow][cNow] == "*":
            continue

        if rNow == lasers[1][0] and cNow == lasers[1][1]:
            return answerNow

        footPrints.add((rNow, cNow))

        for i in range(4):
            rNext = rNow + dr[i]
            cNext = cNow + dc[i]

            if rNext < 0 or cNext < 0 or rNext >= r or cNext >= c:
                continue

            if matrix[rNext][cNext] == "*":
                continue

            if i == 0 and dNow == 2:
                continue
            if i == 1 and dNow == 3:
                continue
            if i == 2 and dNow == 0:
                continue
            if i == 3 and dNow == 1:
                continue

            if (rNext, cNext) in footPrints:
                continue

            if i == dNow:
                queue.put((answerNow, (rNext, cNext, i)))

            else:
                queue.put((answerNow + 1, (rNext, cNext, i)))


c, r = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(r)]

lasers = []

answer = 0

for i in range(r):
    for j in range(c):

        if matrix[i][j] == 'C':
            lasers += [[i, j]]

answer = bfs(lasers)

print(answer)