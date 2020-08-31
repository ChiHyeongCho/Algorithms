
from collections import deque
import copy

def bfsOne(r, c):

    queue = deque()
    queue.append((r, c))

    footPrints = set()
    end = ()
    local = 0

    # 최단경로 탐색
    while queue:

        nr, nc = queue.popleft()
        footPrints.add((nr, nc))

        if nr == 0 or nr == h-1 or nc == 0 or nc == w-1:
            end += (nr, nc)
            break


        for k in range(4):

            ar = nr + dr[k]
            ac = nc + dc[k]

            if 0 <= ar < h and 0 <= ac < w:
                if (ar, ac) not in  footPrints:
                    if matrix[ar][ac] == "#" or matrix[ar][ac] == ".":

                        queue.append((ar, ac))
                        footPrints.add((ar, ac))
                        matrix[ar][ac] = "."

    # 최소 문 구하기
    queue = deque()
    queue.append((end[0], end[1]))
    copyMatrix[end[0]][end[1]] = "."
    footPrints = set()


    while queue:

        nr, nc = queue.popleft()
        footPrints.add((nr, nc))

        if nr == r and nc == c:
            break

        for k in range(4):

            ar = nr + dr[k]
            ac = nc + dc[k]

            if 0 <= ar < h and 0 <= ac < w:
                if (ar, ac) not in footPrints:
                    if matrix[ar][ac] == ".":
                        queue.append((ar, ac))
                        footPrints.add((ar, ac))

                    if copyMatrix[ar][ac] == "#":
                        copyMatrix[ar][ac] = "."
                        local += 1

    print(matrix)
    print(copyMatrix)

    return local



T = int(input())

for _ in range(T):

    # 전처리

    h, w = map(int, input().split())

    matrix = [list(input()) for _ in range(h)]
    copyMatrix = copy.deepcopy(matrix)

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    persons = []

    for i in range(h):
        for j in range(w):

            if matrix[i][j] == "$":
                persons += [i, j]
                matrix[i][j] == ""

    one = (persons[0], persons[1])
    two = (persons[2], persons[3])

    # 문제풀이

    answer = 0

    # 두개 다 최소일 경우

    localAnswerOne = 0
    localAnswerOne = bfsOne(one[0], one[1]) + bfsOne(two[0], two[1])

    print(localAnswerOne)

    # 합쳐서 최소일 경우

    localAnswerTwo = 0

    answer = min(localAnswerOne, localAnswerTwo)

    #print(answer)