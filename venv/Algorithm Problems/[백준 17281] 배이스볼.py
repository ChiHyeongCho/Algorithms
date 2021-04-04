
from itertools import permutations

n = int(input())
player = [i+1 for i in range(9)]
matrix = [list(map(int, input().split())) for _ in range(n)]


permutation = list(permutations(player[1:9]))
permutationsPlayer = []
answer = 0

for i in permutation:

    temp = list(i)
    temp.insert(3, 1)
    permutationsPlayer += [temp]

for i in permutationsPlayer:

    nowPermutations = i
    gameCount = 0
    playerCount = 0
    localAnswer = 0

    #print(i)

    while True:

        if gameCount == n:
            if answer < localAnswer:
                answer = localAnswer
            break

        outCount = 0
        position = [0, 0, 0]

        while True:

            if playerCount >= 9:
                playerCount = 0

            nowPlayer = matrix[gameCount][nowPermutations[playerCount] - 1]

            #print(nowPlayer, outCount, [nowPermutations[playerCount]])

            if outCount == 3:
                gameCount += 1
                break

            if nowPlayer == 0:
                outCount += 1
                playerCount += 1

            elif nowPlayer == 1:
                if position[2] == 1:
                    position[2] = 0
                    localAnswer += 1
                position[2] = position[1]
                position[1] = position[0]
                position[0] = 1
                playerCount += 1

            elif nowPlayer == 2:
                if position[2] == 1:
                    position[2] = 0
                    localAnswer += 1
                if position[1] == 1:
                    position[1] = 0
                    localAnswer += 1
                position[2] = position[0]
                position[0] = 0
                position[1] = 1
                playerCount += 1

            elif nowPlayer == 3:
                if position[2] == 1:
                    position[2] = 0
                    localAnswer += 1
                if position[1] == 1:
                    position[1] = 0
                    localAnswer += 1
                if position[0] == 1:
                    position[0] = 0
                    localAnswer += 1
                position[2] = 1
                playerCount += 1

            else:
                if position[2] == 1:
                    position[2] = 0
                    localAnswer += 1
                if position[1] == 1:
                    position[1] = 0
                    localAnswer += 1
                if position[0] == 1:
                    position[0] = 0
                    localAnswer += 1

                localAnswer += 1
                playerCount += 1

    #print(answer)
print(answer)