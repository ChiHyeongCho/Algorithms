
from copy import deepcopy

class fish:

    def __init__(self, r, c, no, dir):
        self.r = r
        self.c = c
        self.no = no
        self.dir = dir


def dfs(matrix, fishes, shark):

    # 물고기 이동
    moveFish(matrix, fishes, shark)

    tempMatrix = deepcopy(matrix)
    tempFishes = deepcopy(fishes)
    tempShark = deepcopy(shark)

    # 상어 이동
    for i in range(1, 4):

        ar = shark[0] + dr[shark[2]] * i
        ac = shark[1] + dc[shark[2]] * i

        if 0 <= ar < 4 and 0 <= ac < 4 and matrix[ar][ac] != 0:

            shark[0] = ar
            shark[1] = ac
            shark[2] = matrix[ar][ac].dir
            shark[3] += matrix[ar][ac].no
            matrix[ar][ac] = 0

            for j in range(len(fishes)):
                if fishes[j].r == ar and fishes[j].c == ac:
                    del fishes[j]
                    break

            dfs(matrix, fishes, shark)

            matrix = deepcopy(tempMatrix)
            fishes = deepcopy(tempFishes)
            shark = deepcopy(tempShark)

    global answer
    if answer < shark[3]:
        answer = shark[3]

    return


def moveFish(matrix, fishes, shark):

    for i in range(len(fishes)):

        rnow, cnow = fishes[i].r, fishes[i].c

        ar = rnow + dr[fishes[i].dir]
        ac = cnow + dc[fishes[i].dir]

        if (0 <= ar < 4 and 0 <= ac < 4 and (ar != shark[0] or ac != shark[1])):

            if matrix[ar][ac] != 0:

                for j in range(len(fishes)):

                    if fishes[j].r == ar and fishes[j].c == ac:
                        matrix[ar][ac], matrix[rnow][cnow] = matrix[rnow][cnow], matrix[ar][ac]
                        fishes[i].r = ar
                        fishes[i].c = ac
                        fishes[j].r = rnow
                        fishes[j].c = cnow
                        break

            else:
                matrix[rnow][cnow] = 0
                matrix[ar][ac] = fishes[i]
                fishes[i].r = ar
                fishes[i].c = ac

        else:

            for j in range(1, 9):

                state = False
                adir = (fishes[i].dir + j)%8

                ar = rnow + dr[adir]
                ac = cnow + dc[adir]

                if (0 <= ar < 4 and 0 <= ac < 4 and (ar != shark[0] or ac != shark[1])):

                    if matrix[ar][ac] != 0:

                        for k in range(len(fishes)):

                            if fishes[k].r == ar and fishes[k].c == ac:
                                matrix[ar][ac], matrix[rnow][cnow] = matrix[rnow][cnow], matrix[ar][ac]
                                fishes[i].dir = adir
                                fishes[i].r = ar
                                fishes[i].c = ac
                                fishes[k].r = rnow
                                fishes[k].c = cnow
                                state = True
                                break

                        if state == True:
                            break

                    else:
                        matrix[rnow][cnow] = 0
                        matrix[ar][ac] = fishes[i]
                        fishes[i].r = ar
                        fishes[i].c = ac
                        fishes[i].dir = adir
                        break


# 좌표, 번호, 방향
fishes = []
matrix = [[list()]*4 for _ in range(4)]
answer = 0

for i in range(4):

    a, b, c, d, e, f, g, h = map(int, input().split())
    fishes += [fish(i, 0, a, b-1)]
    fishes += [fish(i, 1, c, d-1)]
    fishes += [fish(i, 2, e, f-1)]
    fishes += [fish(i, 3, g, h-1)]

fishes.sort(key = lambda x:x.no)

# 상어 좌표, 방향, 먹이
shark = [0, 0, 0, 0]

# 위쪽부터 반시계방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
dm = ["↑", "↖", "←", "↙", "↓", "↘", "→", "↗"]

for i in range(len(fishes)):

    x, y, no, dir = fishes[i].r, fishes[i].c, fishes[i].no, fishes[i].dir
    matrix[x][y] = fishes[i]


for i in range(len(fishes)):

    x, y, no, dir = fishes[i].r, fishes[i].c, fishes[i].no, fishes[i].dir
    if x == 0 and y == 0:
        shark[2] = dir
        shark[3] = no
        matrix[x][y] = 0
        del fishes[i]
        break

dfs(matrix, fishes, shark)

print(answer)
