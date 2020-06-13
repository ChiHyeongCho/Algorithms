
def dfs(r, c, cnt):

    if cnt == 5:

        newString = ""

        for i in range(6):

            newString += str(int_list[i])

        foot_prints.add(int(newString))

        return

    for i in range(4):

        ar = dr[i] + r
        ac = dc[i] + c

        if 0 <= ar < 5 and 0 <= ac < 5:

            int_list[cnt+1] = matrix[ar][ac]
            dfs(ar, ac, cnt + 1)
            int_list[cnt+1] = 0

matrix = [list(map(int, input().split())) for _ in range(5)]

foot_prints = set()

int_list = [0]*6

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(5):
    for j in range(5):

        int_list[0] = matrix[i][j]
        dfs(i, j, 0)

print(len(foot_prints))