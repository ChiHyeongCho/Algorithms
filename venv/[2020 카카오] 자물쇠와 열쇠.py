import copy

def turnKey(array):

    n = len(array)
    ret = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = array[r][c]

    return ret


def check(boardArray, keyArray, r, c):

    checkArray = copy.deepcopy(boardArray)

    for i in range(len(keyArray)):
        for j in range(len(keyArray)):

            checkArray[r+i][c+j] += keyArray[i][j]


    for i in range(len(keyArray)-1, len(checkArray) - len(keyArray)+1):
        for j in range(len(keyArray) - 1, len(checkArray) - len(keyArray)+1):

            if checkArray[i][j] == 0 or checkArray[i][j] == 2:
                return False

    return True


def solution(key, lock):

    # 문제 정의

    answer = False
    keyLen = len(key)
    lockLen = len(lock)

    count = 0

    for i in range(lockLen):
        for j in range(lockLen):

            if lock[i][j] == 1:
                count += 1

    if count == lockLen**2:
        answer = True
        return answer


    board = [[0]*(keyLen+lockLen+1) for _ in range(keyLen+lockLen+1)]

    for i in range(lockLen):
        for j in range(lockLen):

            board[i+keyLen-1][j+keyLen-1] = lock[i][j]


    print(board)

    # 문제 풀이
    for k in range(4):

        key = turnKey(key)

        for i in range(0, keyLen+lockLen-1):
            for j in range(0, keyLen+lockLen-1):

                answer = check(board, key, i, j)

                if answer == True:
                    break

            if answer == True:
                break

        if answer == True:
            break

    return answer



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))