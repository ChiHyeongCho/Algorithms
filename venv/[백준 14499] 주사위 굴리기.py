class dice:

    def __init__(self, x, y, a, b, c, d, e, f):

        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


def east():

    ar = dice_now.x + dr[0]
    ac = dice_now.y + dc[0]

    if 0 <= ar < R and 0 <= ac < C:

        dice_now.x = ar
        dice_now.y = ac

        temp = dice_now.a

        dice_now.a = dice_now.e
        dice_now.e = dice_now.f
        dice_now.f = dice_now.c
        dice_now.c = temp

        if matrix[ar][ac] == 0:

            matrix[ar][ac] = dice_now.f

        else:

            dice_now.f = matrix[ar][ac]
            matrix[ar][ac] = 0

        #print(matrix)
        #print(dice_now.a, dice_now.b, dice_now.c, dice_now.d, dice_now.e, dice_now.f)
        print(dice_now.a)

def west():

    ar = dice_now.x + dr[1]
    ac = dice_now.y + dc[1]

    if 0 <= ar < R and 0 <= ac < C:

        dice_now.x = ar
        dice_now.y = ac

        temp = dice_now.a

        dice_now.a = dice_now.c
        dice_now.c = dice_now.f
        dice_now.f = dice_now.e
        dice_now.e = temp

        if matrix[ar][ac] == 0:

            matrix[ar][ac] = dice_now.f

        else:

            dice_now.f = matrix[ar][ac]
            matrix[ar][ac] = 0

        #print(matrix)
        #print(dice_now.a, dice_now.b, dice_now.c, dice_now.d, dice_now.e, dice_now.f)
        print(dice_now.a)

def north():

    ar = dice_now.x + dr[2]
    ac = dice_now.y + dc[2]

    if 0 <= ar < R and 0 <= ac < C:

        dice_now.x = ar
        dice_now.y = ac

        temp = dice_now.a

        dice_now.a = dice_now.b
        dice_now.b = dice_now.f
        dice_now.f = dice_now.d
        dice_now.d = temp

        if matrix[ar][ac] == 0:

            matrix[ar][ac] = dice_now.f

        else:

            dice_now.f = matrix[ar][ac]
            matrix[ar][ac] = 0

        #print(matrix)
        #print(dice_now.a, dice_now.b, dice_now.c, dice_now.d, dice_now.e, dice_now.f)
        print(dice_now.a)

def south():

    ar = dice_now.x + dr[3]
    ac = dice_now.y + dc[3]

    if 0 <= ar < R and 0 <= ac < C:

        dice_now.x = ar
        dice_now.y = ac

        temp = dice_now.a

        dice_now.a = dice_now.d
        dice_now.d = dice_now.f
        dice_now.f = dice_now.b
        dice_now.b = temp

        if matrix[ar][ac] == 0:

            matrix[ar][ac] = dice_now.f

        else:

            dice_now.f = matrix[ar][ac]
            matrix[ar][ac] = 0

        #print(matrix)
        #print(dice_now.a, dice_now.b, dice_now.c, dice_now.d, dice_now.e, dice_now.f)
        print(dice_now.a)

R, C, r, c, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

order = list(map(int, input().split()))

dice_now = dice(r, c, 0, 0, 0, 0, 0, 0)

for i in order:

    if i == 1:

        east()

    elif i == 2:

        west()

    elif i == 3:
        north()

    else:
        south()
