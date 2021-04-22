
from itertools import combinations
from collections import deque
import copy

def check(r, c):

    queue = deque()
    queue.append((r, c))

    footPrints = set()
    footPrints.add((r, c))

    check = 0

    while queue:

        nr, nc = queue.popleft()
        check += 1

        for k in range(4):

            ar = nr + dr[k]
            ac = nc + dc[k]

            if 0 <= ar < 5 and 0 <= ac < 5:
                if matrix[ar][ac] == 1 and (ar, ac) not in footPrints :

                    queue.append((ar, ac))
                    footPrints.add((ar, ac))

    if check == 7:
        return True
    else:
        return False

def backup():

    for i in range(7):

        r, c, x = orderMatrix[i]
        matrix[r][c] = x



# 전처리

matrix = [list(input()) for _ in range(5)]

answer = 0
combiMatrix = []
Map = {}
mapIndex = 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for i in range(25):
    combiMatrix += [i]

for i in range(5):
    for j in range(5):

        Map[mapIndex] = (i,j)
        mapIndex += 1

combi = list(combinations(combiMatrix, 7))

for i in range(len(combi)):

    defi = 0
    orderMatrix = []

    for j in range(len(combi[i])):

        r, c = Map[combi[i][j]]
        x = copy.deepcopy(matrix[r][c])
        orderMatrix += [[r, c, x]]

        if matrix[r][c] == "S":
            defi += 1

        matrix[r][c] = 1

    if defi >= 4 and check(orderMatrix[0][0], orderMatrix[0][1]):
        answer += 1
    backup()

print(answer)