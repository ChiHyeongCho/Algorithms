class snake():

    def __init__(self, head_r, head_c, tail_r, tail_c, dic, tail_dic):
        self.head_r = head_r
        self.head_c = head_c
        self.tail_r = tail_r
        self.tail_c = tail_c
        self.dic = dic
        self.tail_dic = tail_dic

def check(r, c):

    if 0 <= r < N and 0 <= c < N and matrix[r][c] != 1:
        return False

    else:
        return True


N = int(input())
K = int(input())

matrix = [[0]*N for _ in range(N)]

for i in range(K):

    a, b = map(int, input().split())
    matrix[a-1][b-1] =2

matrix[0][0] = 1

L = int(input())

order = [list(map(str ,input().split())) for _ in range(L)]

time = 1
s = snake(0,0,0,0,0,0)
index = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

tail_time = 0
tail_index = 0

while True:

    #go
    s.head_r += dr[s.dic]
    s.head_c += dc[s.dic]

    now_r = s.head_r
    now_c = s.head_c

    if check(now_r, now_c):
        print(time)
        break

    default = matrix[now_r][now_c]
    matrix[now_r][now_c] = 1


    if default != 2:

        matrix[s.tail_r][s.tail_c] = 0
        s.tail_r += dr[s.tail_dic]
        s.tail_c += dc[s.tail_dic]
        tail_time += 1

        if tail_index < L and tail_time == int(order[tail_index][0]):

            if order[tail_index][1] == "D":
                s.tail_dic += 1

                if s.tail_dic == 4:
                    s.tail_dic = 0

            else:

                s.tail_dic -= 1

                if s.tail_dic == -1:
                    s.tail_dic = 3

            tail_index += 1


    if index < L and time == int(order[index][0]):

        if order[index][1] == "D":
            s.dic += 1

            if s.dic == 4:
                s.dic = 0

        else:

            s.dic -= 1

            if s.dic == -1:
                s.dic = 3

        index += 1

    time += 1