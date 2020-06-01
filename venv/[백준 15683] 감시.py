from collections import deque
import copy

def watch_cam(dic, r, c, num):

    ar = r + dr[dic]
    ac = c + dc[dic]

    if 0 <= ar < N and 0 <= ac < M:
        if matrix[ar][ac] <= 0:
            matrix[ar][ac] += num
            watch_cam(dic, ar, ac, num)

        elif matrix[ar][ac] == 6:
            return

        else:
            watch_cam(dic, ar, ac, num)



def check():

    Sum = 0

    for i in range(N):
        for j in range(M):

           if matrix[i][j] == 0:
               Sum += 1

    return Sum


def dfs(order, matrix):

    global region

    if order == len(cameras):

        local = check()

        if local < region:
            region = local

        return

    r, c, Type = cameras[order]

    if Type == 1:

        for dic in range(4):

            watch_cam(dic, r, c, -1)
            dfs(order+1, matrix)
            watch_cam(dic, r, c, 1)

    elif Type == 2:

        for dic in range(2):

            watch_cam(dic, r, c, -1)
            watch_cam(dic+2, r, c, -1)
            dfs(order+1, matrix)
            watch_cam(dic, r, c, 1)
            watch_cam(dic+2, r, c, 1)

    elif Type == 3:

        for dic in range(4):

            watch_cam(dic, r, c, -1)
            watch_cam((dic+1)%4, r, c, -1)
            dfs(order+1, matrix)
            watch_cam(dic, r, c, 1)
            watch_cam((dic+1)%4, r, c, 1)

    elif Type == 4:

        for dic in range(4):

            watch_cam(dic, r, c, -1)
            watch_cam((dic+1)%4, r, c, -1)
            watch_cam((dic+2)%4, r, c, -1)
            dfs(order+1, matrix)
            watch_cam(dic, r, c, 1)
            watch_cam((dic+1)%4, r, c, 1)
            watch_cam((dic+2)%4, r, c, 1)

    elif Type == 5:

        watch_cam(0, r, c, -1)
        watch_cam(1, r, c, -1)
        watch_cam(2, r, c, -1)
        watch_cam(3, r, c, -1)
        dfs(order+1, matrix)
        watch_cam(0, r, c, 1)
        watch_cam(1, r, c, 1)
        watch_cam(2, r, c, 1)
        watch_cam(3, r, c, 1)

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
cameras = deque()

dr = [1,0,-1,0]
dc = [0,-1,0,1]


for i in range(N):
    for j in range(M):

        if matrix[i][j] != 6 and matrix[i][j] != 0:
            cameras.append((i, j, matrix[i][j]))


region = 8*8
dfs(0, matrix)
print(region)