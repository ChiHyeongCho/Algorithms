import sys


def to_num(x, y):
    return ord(matrix[x][y]) - ord('A')


def dfs(nr, nc, localAnswer):

    for i in range(4):

        ar = nr + dr[i]
        ac = nc + dc[i]

        if 0 <= ar < r and 0 <= ac < c:

            if visited[to_num(ar, ac)] == 0:

                visited[to_num(ar, ac)] = 1
                dfs(ar, ac, localAnswer+1)
                visited[to_num(ar, ac)] = 0

            else:

                global answer
                if answer < localAnswer:
                    answer = localAnswer


r, c = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

matrix = [list(sys.stdin.readline().strip()) for _ in range(r)]

answer = 0
visited = [0]*26

visited[to_num(0, 0)] = 1

dfs(0, 0, 1)

print(answer)


