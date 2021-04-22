def check(r, c, x):

    if r1 <= r <= r2 and c1 <= c <= c2:

        if r1 < 0 and c1 < 0:

            answer[r + max_index][c + max_index] = str(x)

        else:

            answer[r][c] = str(x)

    return

r1, c1, r2, c2 = map(int, input().split())

answer = [[0]*(abs(c2-c1)+1) for _ in range(abs(r2-r1)+1)]

max_index = max(abs(r1), abs(c1), abs(r2), abs(c2))

start_index = 0
start_rcx = [0, 0, 1]

while True:

    r, c, x = start_rcx[0], start_rcx[1], start_rcx[2]

    check(r, c, x)

    if r == max_index and c == max_index:
        break

    ar = r
    ac = c + 1
    ax = x + 1

    check(ar, ac, ax)

    start_index += 1

    for i in range(start_index):

        ar = ar - 1
        ac = ac
        ax = ax + 1
        check(ar, ac, ax)

    start_index += 1

    for i in range(start_index):

        ar = ar
        ac = ac - 1
        ax = ax + 1
        check(ar, ac, ax)

    for i in range(start_index):
        ar = ar + 1
        ac = ac
        ax = ax + 1
        check(ar, ac, ax)

    for i in range(start_index):
        ar = ar
        ac = ac + 1
        ax = ax + 1
        check(ar, ac, ax)

    start_rcx[0] = ar
    start_rcx[1] = ac
    start_rcx[2] = ax

a = len(answer[0][0])
b = len(answer[0][c2-c1])
c = len(answer[r2-r1][0])
d = len(answer[r2-r1][c2-c1])

max_len = max(a, b, c ,d)

for i in range((abs(r2-r1)+1)):
    for j in range((abs((c2-c1) + 1))):

        if len(answer[i][j]) <= max_len:

            print(" " * (max_len - len(answer[i][j])) + answer[i][j], end = " ")
    print()









