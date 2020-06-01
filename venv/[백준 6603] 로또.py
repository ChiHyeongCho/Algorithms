def dfs(start, depth, end):

    if depth == 6:
        for i in range (6):

            print(combi[i], end = " ")
        print()
        return

    for i in range(start, end):

        combi[depth] = Str[i]
        dfs(i+1, depth+1, end)
        combi[depth] = 0


while True:

    Str = list(map(int, input().split()))

    if Str[0] == 0:
        break

    combi = [0]*6

    del Str[0]

    dfs(0 , 0, len(Str))

    print()