
def rotate_90(m):

    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]

    return ret


print(rotate_90([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))