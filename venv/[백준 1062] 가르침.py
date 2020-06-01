
def dfs(start, cnt):

    global answer

    if cnt == K:

        local = N

        for i in range(N):

            for j in range(len(words[i])):

                if visited[Map[words[i][j]]] == 0:

                    local -= 1
                    break

        if local > answer:

            answer = local

        return


    for i in range(start, 26):

        if visited[i] != 1:

            visited[i] = 1

            dfs(i, cnt+1)

            visited[i] = 0



N, K = map(int, input().split())

words = []

for i in range(N):

    words += [input()]

alpabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i" , "j" , "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

Map = {}

for i in range(26):

    Map.update({alpabet[i] : i})


visited = [0]*26

combination = [0]*K

answer = 0

dfs(0, 0)

print(answer)