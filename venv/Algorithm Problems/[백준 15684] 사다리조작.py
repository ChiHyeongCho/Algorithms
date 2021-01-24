
def dfs(a, b, cnt):

    global answer

    if cnt > 3 or cnt >= answer:
        return

    state = True

    for i in range(c):

        h_c = i

        for j in range(r):

            if matrix[j][h_c] == 1:

                h_c += 1

            elif h_c - 1 >= 0 and matrix[j][h_c - 1] == 1:

                h_c -= 1


        if h_c != i:
            state = False
            break


    if state == True:

        if answer > cnt:
            answer = cnt

        return

    else:

        for i in range(a, r):

            if i == a:

                for j in range(b, c-1):

                    if matrix[i][j] != 1:

                        if 0 < j and matrix[i][j - 1] != 1 and matrix[i][j + 1] != 1:

                            matrix[i][j] = 1
                            dfs(i, j, cnt + 1)
                            matrix[i][j] = 0

                        elif j == 0 and matrix[i][j + 1] != 1:

                            matrix[i][j] = 1
                            dfs(i, j, cnt + 1)
                            matrix[i][j] = 0

            else:

                for j in range(c-1):

                    if matrix[i][j] != 1:

                        if 0 < j  and matrix[i][j-1] != 1 and matrix[i][j+1] != 1:

                            matrix[i][j] = 1
                            dfs(i, j, cnt + 1)
                            matrix[i][j] = 0

                        elif j == 0 and matrix[i][j+1] != 1:

                            matrix[i][j] = 1
                            dfs(i, j, cnt + 1)
                            matrix[i][j] = 0


c, H, r = map(int, input().split())

matrix = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]

for i in range(H):

    a, b = map(int, input().split())

    matrix[a-1][b-1] = 1

answer = 100

dfs(0, 0, 0)

if answer == 100:
    print(-1)

else:
    print(answer)