
from _collections import deque

def breakMi(direction, row):

    if direction == 1:

        for i in range(c):

            if matrix[len(matrix)-row][i] == "x":
                matrix[len(matrix)-row][i] = "."
                break
    else:
        for i in range(c):

            if matrix[len(matrix)-row][c-i-1] == "x":
                matrix[len(matrix)-row][c-i-1] = "."
                break


def isPossibleStand():

    footPrtins = set()
    queue = deque()
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for i in range(r):
        for j in range(c):

            if matrix[i][j] == "x" and (i, j) not in footPrtins:

                state = False

                cluster = []
                cluster += [[i, j]]
                queue.append((i, j))
                footPrtins.add((i, j))

                if i == r-1:
                    state = True

                while queue:

                    nr, nc = queue.popleft()

                    for k in range(4):

                        ar = nr + dr[k]
                        ac = nc + dc[k]

                        if 0 <= ar < r and 0 <= ac < c:
                            if (ar, ac) not in footPrtins:
                                if matrix[ar][ac] == "x":

                                    queue.append((ar, ac))
                                    footPrtins.add((ar, ac))
                                    cluster += [[ar, ac]]

                                    if ar == r-1:
                                        state = True

                #print(state)
                #print(cluster)
                if state == False:

                    for a, b in cluster:

                        matrix[a][b] = "."

                    while True:

                        stateLocal = True

                        for k in range(len(cluster)):

                            if cluster[k][0] + 1 >= r or matrix[cluster[k][0] + 1][cluster[k][1]] == "x":
                                stateLocal = False

                        if stateLocal == False:
                            break

                        else:
                            for k in range(len(cluster)):
                                cluster[k][0] += 1

                    for a, b in cluster:

                        matrix[a][b] = "x"

                    return


r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
m = int(input())
orders = list(map(int, input().split()))

for i in range(len(orders)):

    if i % 2 == 0:
        breakMi(1, orders[i])
        isPossibleStand()
    else:
        breakMi(-1, orders[i])
        isPossibleStand()

    #for j in range(len(matrix)):

     #   print(matrix[j])

    #print()


for i in range(r):
    for j in range(c):

        print(matrix[i][j], end = "")

    print()