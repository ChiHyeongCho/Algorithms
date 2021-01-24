
from collections import deque

def dfs(r, c):

    global answer

    if r == N-1 and c == M-1:
        answer +=1
        return

    for i in range(4):

        ar = r + dr[i]
        ac = c + dc[i]

        if 0 <= ar < N and 0 <= ac < M:
            if visited[ar][ac] != 1 and matrix[r][c] > matrix[ar][ac]:

                visited[ar][ac] = 1
                dfs(ar, ac)
                visited[ar][ac] = 0


N, M = map(int, input().split())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
answer = 0
dfs(0,0)
print(answer)