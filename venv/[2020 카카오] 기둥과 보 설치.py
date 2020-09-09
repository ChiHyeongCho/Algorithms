

def solution(n, build_frame):

    # 문제 정의
    answer = []
    matrix = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):

            matrix[i][j] = set()

    # 문제 풀이

    for i in range(len(build_frame)):


        x, y, a, b = build_frame[i]

        print(i)

        for i in range(5, -1, -1):
            print(matrix[i])

        if b != 0:

            if a == 0:

                if y == 0 or (y >= 1 and len(matrix[x][y-1]) != 0) or (x >= 1 and len(matrix[x-1][y]) != 0):
                    matrix[x][y].add(0)

                else:
                    continue

            else:

                if x != n or (x >= 1 and 0 in matrix[x-1][y-1]) or (x >= 1 and 1 in matrix[x-1][y] and 1 in matrix[x+1][y]):
                    matrix[x][y].add(1)

                else:
                    continue


        else:

            if a == 0:

                if 1 in matrix[x-1][y+1] and 1 in matrix[x+1][y+1]:
                    matrix[x][y].pop(0)

                elif

            else:
                matrix[x][y].pop(-1)

    answer = sorted(answer, key = lambda x:(x[0], x[1]))

    index = 0


    return answer



print(solution(5,	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))