
n = int(input())

matrix = [[0] * 101 for _ in range(101)]
dragonCurve = [list(map(int, input().split())) for _ in range(n)]


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for i in dragonCurve:

    count = 0
    c, r, dir, generation = i

    #matrix = [[0] * 100 for _ in range(100)]

    rotateR = r + dr[dir]
    rotateC = c + dc[dir]

    dargonCurveSet = set()
    dargonCurveSet.add((r, c))
    dargonCurveSet.add((rotateR, rotateC))
    tempSet = set()
    nextRotateR = 0
    nextRotateC = 0

    while True:

        #print(rotateR, rotateC)

        if count == generation:
            break

        for k in dargonCurveSet:

            realR, realC = k
            parrelR = realR - rotateR
            parrelC = realC - rotateC

            transR = parrelC
            transC = -parrelR

            tempSet.add((transR + rotateR, transC + rotateC))

            if realR == r and realC == c:
                nextRotateR = transR + rotateR
                nextRotateC = transC + rotateC

        for k in tempSet:

            dargonCurveSet.add(k)

        rotateR = nextRotateR
        rotateC = nextRotateC

   #     print(dargonCurveSet)

        count += 1

    for k in dargonCurveSet:

        a, b = k

        matrix[a][b] = 1

#    for k in matrix:
#        print(k)

#    print()

#for i in matrix:

#    print(i)

answer = 0

for i in range(100):
    for j in range(100):

        if matrix[i][j] == 1 and matrix[i+1][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j+1] == 1:
            answer += 1

print(answer)

