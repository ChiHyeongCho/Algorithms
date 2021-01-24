from collections import deque
import copy

class order:

    def __init__(self, num, dic, iter):

        self.num = num
        self.dic = dic
        self.iter = iter


def move(num, dic, iter):

    if dic == 0:

        for i in range(1, N//num+1):

            transfer = matrix[num*i-1][-iter:] + matrix[num*i-1][:M-iter]
            matrix[num*i-1] = copy.deepcopy(transfer)


    else:

        for i in range(1, N//num+1):

            transfer = matrix[num*i-1][iter:] + matrix[num*i-1][:iter]
            matrix[num*i-1] = copy.deepcopy(transfer)


def Sum_all():

    Sum = 0

    for i in range(N):

        Sum += sum(matrix[i][:])

    return Sum

def find(i,j):

    queue = deque()
    queue.append((i, j))
    foot_prints = set()
    foot_prints.add((i, j))
    check = False

    while queue:

        r, c = queue.popleft()

        for k in range(4):

            ar = r + dr[k]
            ac = c + dc[k]

            if ac == -1:
                ac = M-1

            if ac == M:
                ac = 0

            if 0 <= ar < N and 0 <= ac < M:
                if matrix[ar][ac] == matrix[i][j]:
                    if (ar, ac) not in foot_prints:

                        queue.append((ar, ac))
                        foot_prints.add((ar, ac))
                        matrix[ar][ac] = 0
                        check = True

    if check == True:
        matrix[i][j] = 0

    return check

def matrix_mean():

    Sum = 0
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                Sum += matrix[i][j]
                count += 1

    if count != 0:
        average = Sum/count

        for i in range(N):
            for j in range(M):

                if matrix[i][j] > average:
                    matrix[i][j] -= 1

                elif matrix[i][j] != 0 and matrix[i][j] < average:

                    matrix[i][j] += 1



N, M, T = map(int, input()
              .split())

matrix = [list(map(int, input().split())) for _ in range(N)]
orders = deque()

for _ in range(T):

    n, d, k = map(int, input().split())
    k %= M
    orders.append(order(n, d, k))

time = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while True:

    if time == T:
        print(Sum_all())
        break

    now = orders.popleft()

    move(now.num, now.dic, now.iter)

    state = False

    for i in range(N):
        for j in range(M):

            if matrix[i][j] != 0:
                if find(i, j):
                    state = True


    if state == False:
        matrix_mean()

    time += 1