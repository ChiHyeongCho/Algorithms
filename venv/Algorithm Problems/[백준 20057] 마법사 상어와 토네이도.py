
n = int(input())
matrix = [list(map(int, input().split()))for _ in range(n)]

toPosition = [n//2, n//2]
answer = 0

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

turnCount = 0
moveCount = 0
possibleMove = 1

windLeft = [[0, -2, 5], [1, -1, 10], [-1, -1, 10], [-2, 0, 2], [-1, 0, 7], [1, 0, 7], [2, 0, 2], [-1, 1, 1], [1, 1, 1]]
windRight = [[0, 2, 5], [1, 1, 10], [-1, 1, 10], [-2, 0, 2], [-1, 0, 7], [1, 0, 7], [2, 0, 2], [-1, -1, 1], [1, -1, 1]]
windUp = [[-2, 0, 5], [-1, 1, 10], [-1, -1, 10], [0, 2, 2], [0, 1, 7], [0, -1, 7], [0, -2, 2], [1, -1, 1], [1, 1, 1]]
windDown = [[2, 0, 5], [1, 1, 10], [1, -1, 10], [0, 2, 2], [0, 1, 7], [0, -1, 7], [0, -2, 2], [-1, 1, 1], [-1, -1, 1]]

dir = 0

while True:

    if toPosition == [0, 0]:
        break

    # 토네이도 이동
    toPosition[0] += dr[dir]
    toPosition[1] += dc[dir]

    # 모래 이동

    sand = matrix[toPosition[0]][toPosition[1]]

    #print(sand, toPosition[0], toPosition[1])

    if dir == 0 and sand != 0:

        windSand = 0

        for i in windLeft:

            ar, ac, ratio = i

            afterR = ar + toPosition[0]
            afterC = ac + toPosition[1]

            windSand += int(sand*(ratio*0.01))

            if 0 <= afterR < n and 0 <= afterC < n:
                matrix[afterR][afterC] += int(sand*(ratio*0.01))

            else:
                answer += int(sand*(ratio*0.01))

        if 0 <= toPosition[0] < n and 0 <= toPosition[1]-1 < n:
            matrix[toPosition[0]][toPosition[1] - 1] += sand - windSand
            matrix[toPosition[0]][toPosition[1]] = 0

        else:
            matrix[toPosition[0]][toPosition[1]] = 0
            answer += sand - windSand

    if dir == 1 and sand != 0:

        windSand = 0

        for i in windDown:

            ar, ac, ratio = i

            afterR = ar + toPosition[0]
            afterC = ac + toPosition[1]

            windSand += int(sand * (ratio * 0.01))

            if 0 <= afterR < n and 0 <= afterC < n:
                matrix[afterR][afterC] += int(sand * (ratio * 0.01))

            else:
                answer += int(sand * (ratio * 0.01))

        if 0 <= toPosition[0]+1 < n and 0 <= toPosition[1] < n:
            matrix[toPosition[0] + 1][toPosition[1]] += sand - windSand
            matrix[toPosition[0]][toPosition[1]] = 0

        else:
            matrix[toPosition[0]][toPosition[1]] = 0
            answer += sand - windSand

    if dir == 2 and sand != 0:

        windSand = 0

        for i in windRight:

            ar, ac, ratio = i

            afterR = ar + toPosition[0]
            afterC = ac + toPosition[1]

            windSand += int(sand * (ratio * 0.01))

            if 0 <= afterR < n and 0 <= afterC < n:
                matrix[afterR][afterC] += int(sand * (ratio * 0.01))

            else:
                answer += int(sand * (ratio * 0.01))


        if 0 <= toPosition[0] < n and 0 <= toPosition[1] + 1 < n:
            matrix[toPosition[0]][toPosition[1] + 1] += sand - windSand
            matrix[toPosition[0]][toPosition[1]] = 0

        else:
            matrix[toPosition[0]][toPosition[1]] = 0
            answer += sand - windSand

    if dir == 3 and sand != 0:

        windSand = 0

        for i in windUp:

            ar, ac, ratio = i

            afterR = ar + toPosition[0]
            afterC = ac + toPosition[1]

            windSand += int(sand * (ratio * 0.01))

            if 0 <= afterR < n and 0 <= afterC < n:
                matrix[afterR][afterC] += int(sand * (ratio * 0.01))

            else:
                answer += int(sand * (ratio * 0.01))

        if 0 <= toPosition[0] - 1 < n and 0 <= toPosition[1] < n:
            matrix[toPosition[0] - 1][toPosition[1]] += sand - windSand
            matrix[toPosition[0]][toPosition[1]] = 0

        else:
            matrix[toPosition[0]][toPosition[1]] = 0
            answer += sand - windSand

    moveCount += 1

    if moveCount == possibleMove:
        moveCount = 0
        dir = (dir+1)%4
        turnCount += 1

    if turnCount == 2:
        possibleMove += 1
        turnCount = 0


    #print(answer)

print(answer)