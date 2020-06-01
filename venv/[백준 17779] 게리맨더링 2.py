

def region_A(r, c, ar, ac):

    a = 0
    index = c+1

    for i in range(ar):

        for j in range(index):

            a += matrix[i][j]

        if i >= r-1:

            index -= 1

    return a

def region_B(r, c, ar, ac):

    b = 0
    index = c+1

    for i in range(ar+1):

        for j in range(index, N):

            b += matrix[i][j]

        if i > r-1:
            index += 1

    return b

def region_C(r, c, ar, ac):

    cx = 0
    index = c

    for i in range(r, N):

        for j in range(index):

            cx += matrix[i][j]

        if i < ar:

            index += 1

    return cx

def region_D(r, c, ar, ac):

    d = 0
    index = c

    for i in range(r+1, N):

        for j in range(index, N):

            d += matrix[i][j]

        if i <= ar:

            index -= 1

    return d

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

All = 0

for i in range(N):

    All += sum(matrix[i])

answer = 100*20*20

for i in range(1, N):
    for j in range(1, N):

        R, C = i, j

        for d1 in range(1, C+1):
            for d2 in range(1, N-C+1):

                if d1 + d2 <= N-R:

                    a = region_A(R, C, R+d1, C-d1)
                    b = region_B(R, C, R+d2, C+d2)
                    c = region_C(R+d1, C-d1, R+d1+d2, C-d1+d2)
                    d = region_D(R+d2, C+d2, R+d2+d1, C+d2-d1)
                    e = All - a - b - c- d

                    local = max(a, b, c, d, e) - min(a, b, c, d, e)

                    if local < answer:

                        answer = local
print(answer)
