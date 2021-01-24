
def dfs(start, end):

    if end == M:
        for k in range(N):
            if visited[k] == 1:
                print(k+1, end = " ")
        print("")
        return

    for k in range(start+1, N):
        if visited[k] != 1:
            visited[k] = 1
            dfs(k, end+1)
            visited[k] = 0





N, M = map(int, input().split())

for i in range(0, N):

    visited = [0]*N
    visited[i] = 1
    dfs(i, 1)


