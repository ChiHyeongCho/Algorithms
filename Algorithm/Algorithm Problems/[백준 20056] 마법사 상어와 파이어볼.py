
from collections import deque

class fireball:

    def __init__(self, r, c, w, s, d):
        self.r_ = r
        self.c_ = c
        self.w_ = w
        self.s_ = s
        self.d_ = d

def move(fireball):

    if fireball.d_ == 0:
        shiftRow = 0
        shiftRow = fireball.r_ - fireball.s_%n
        if shiftRow < 0:
            shiftRow = fireball.r_ + n - fireball.s_%n
        fireball.r_ = shiftRow

    if fireball.d_ == 2:
        shiftCol = 0
        shiftCol = fireball.c_ + fireball.s_%n
        if shiftCol >= n:
            shiftCol = fireball.c_ - (n - fireball.s_%n)
        fireball.c_ = shiftCol

    if fireball.d_ == 4:
        shiftRow = 0
        shiftRow = fireball.r_ + fireball.s_%n
        if shiftRow >= n:
            shiftRow = fireball.r_ - (n - fireball.s_%n)
        fireball.r_ = shiftRow

    if fireball.d_ == 6:
        shiftCol = 0
        shiftCol = fireball.c_ - fireball.s_%n
        if shiftCol < 0:
            shiftCol = fireball.c_ + n - fireball.s_%n
        fireball.c_ = shiftCol

    if fireball.d_ == 1:
        shiftRow = 0
        shiftRow = fireball.r_ - fireball.s_%n
        if shiftRow < 0:
            shiftRow = fireball.r_ + n - fireball.s_%n
        fireball.r_ = shiftRow
        shiftCol = 0
        shiftCol = fireball.c_ + fireball.s_%n
        if shiftCol >= n:
            shiftCol = fireball.c_ - (n - fireball.s_%n)
        fireball.c_ = shiftCol

    if fireball.d_ == 3:
        shiftCol = 0
        shiftCol = fireball.c_ + fireball.s_%n
        if shiftCol >= n:
            shiftCol = fireball.c_ - (n - fireball.s_%n)
        fireball.c_ = shiftCol
        shiftRow = 0
        shiftRow = fireball.r_ + fireball.s_%n
        if shiftRow >= n:
            shiftRow = fireball.r_ - (n - fireball.s_%n)
        fireball.r_ = shiftRow

    if fireball.d_ == 5:
        shiftCol = 0
        shiftCol = fireball.c_ - fireball.s_%n
        if shiftCol < 0:
            shiftCol = fireball.c_ + n - fireball.s_%n
        fireball.c_ = shiftCol
        shiftRow = 0
        shiftRow = fireball.r_ + fireball.s_%n
        if shiftRow >= n:
            shiftRow = fireball.r_ - (n - fireball.s_%n)
        fireball.r_ = shiftRow

    if fireball.d_ == 7:
        shiftRow = 0
        shiftRow = fireball.r_ - fireball.s_%n
        if shiftRow < 0:
            shiftRow = fireball.r_ + n - fireball.s_%n
        fireball.r_ = shiftRow
        shiftCol = 0
        shiftCol = fireball.c_ - fireball.s_%n
        if shiftCol < 0:
            shiftCol = fireball.c_ + n - fireball.s_%n
        fireball.c_ = shiftCol

    matrix[fireball.r_][fireball.c_].append(fireball)

def mergeSplit(j, k, fireballs, newFireballs):

    weightSum = 0
    speedSum = 0
    directionSum = 0

    for i in range(len(matrix[j][k])):

        weightSum += matrix[j][k][i].w_
        speedSum += matrix[j][k][i].s_
        directionSum += matrix[j][k][i].d_%2

    afterWeight = weightSum//5
    afterSpeed = speedSum//len(matrix[j][k])

    if afterWeight > 0:
        if directionSum == 0 or directionSum == len(matrix[j][k]):
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 0)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 2)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 4)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 6)]

        else:
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 1)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 3)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 5)]
            newFireballs += [fireball(j, k, afterWeight, afterSpeed, 7)]


n, m, k = map(int, input().split())

fireballs = []
totalWeight = 0

for i in range(m):

    # 0 : 행, 1 : 열, 2 : 질량, 3 : 속력, 4 : 방향
    tempInput = list(map(int, input().split()))
    fireballs += [fireball(tempInput[0]-1, tempInput[1]-1, tempInput[2], tempInput[3], tempInput[4])]

for i in range(k):

    matrix = [[0] * n for _ in range(n)]
    newFireballs = []

    for j in range(n):
        for k in range(n):
            matrix[j][k] = deque()

    for j in range(len(fireballs)):

        move(fireballs[j])

#    for j in range(len(fireballs)):
#        print(fireballs[j].r_, fireballs[j].c_)

    for j in range(n):
        for l in range(n):

            if len(matrix[j][l]) > 1:

                mergeSplit(j, l, fireballs, newFireballs)

            else:

                newFireballs += matrix[j][l]


  #  print(len(newFireballs))

    fireballs = newFireballs
   # for j in range(len(fireballs)):
    #    print(fireballs[j].r_, fireballs[j].c_, fireballs[j].w_, fireballs[j].s_, fireballs[j].d_)

 #   print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


for i in range(len(fireballs)):
    totalWeight += fireballs[i].w_

print(totalWeight)






