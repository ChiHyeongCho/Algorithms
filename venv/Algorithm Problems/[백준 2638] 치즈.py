import sys
from collections import deque

def findCheese():

    for i in range(r):
        for j in range(c):

            if matrix[i][j] == 1:
                return False
    return True


def findOutsideAir():

    queue = deque()
    footPrints = set()
    queue.append((0, 0))
    footPrints.add((0, 0))

    dr = [0, 1, -1, 0]
    dc = [1, 0, 0, -1]

    while queue:

        rNow, cNow = queue.popleft()

        for i in range(4):

            ar = rNow + dr[i]
            ac = cNow + dc[i]

            if 0 <= ar < r and 0 <= ac < c:

                if (matrix[ar][ac] == 0 or matrix[ar][ac] == 2) and (ar, ac) not in footPrints:
                    queue.append((ar, ac))
                    footPrints.add((ar, ac))
                    matrix[ar][ac] = 2
    return


def findRemoveCheese(removeCheeses):

    dr = [0, 1, -1, 0]
    dc = [1, 0, 0, -1]

    for i in range(r):
        for j in range(c):

            if matrix[i][j] == 1:

                count = 0

                for k in range(4):

                    ar = dr[k] + i
                    ac = dc[k] + j

                    if 0 <= ar < r and 0 <= ac < c:
                        if matrix[ar][ac] == 2:
                            count += 1

                if count >= 2:
                    removeCheeses.append((i, j))

    return


def removeCheese(removeCheeses):

    for i, j in removeCheeses:

        matrix[i][j] = 2

    return


r, c = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]


time = 0

while True:

    if findCheese():
        break

    else:
        time += 1
        findOutsideAir()
        removeCheeses = deque()
        findRemoveCheese(removeCheeses)
        removeCheese(removeCheeses)


print(time)