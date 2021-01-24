from collections import deque

def bfs(i):

    queue.append(i)
    foot_prints.add(i)
    n = -1

    while queue:

        j = queue.popleft()
        n += 1

        for k in range(N):
            if k not in foot_prints and visited[j][k] == 1:
                queue.append(k)
                foot_prints.add(k)

    return n

N = int(input())
num = int(input())

visited = [[0]*N for _ in range(N)]

for i in range(num):

    r, c = map(int, input().split())

    visited[r-1][c-1] = 1
    visited[c-1][r-1] = 1

foot_prints = set()
queue = deque()
print(bfs(0))