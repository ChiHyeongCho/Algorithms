
import sys
from collections import deque
import math

def possibleMeet(start, time):

    queue = deque()
    footPrints = set()

    i = start[0]
    j = start[1]

    queue.append((i, j))
    footPrints.add((i, j))

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:

        rNow, cNow = queue.popleft()

        for k in range(4):

            ar = rNow + dr[k]
            ac = cNow + dc[k]

            if 0 <= ar < r and 0 <= ac < c:

                if matrixBfs[ar][ac] <= time and (ar, ac) not in footPrints:
                    queue.append((ar, ac))
                    footPrints.add((ar, ac))

                    if ar == end[0] and ac == end[1]:
                        return True

    return False


def updateMatrix():

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    footPrints = set()
    meltTime = 0

    while globalWillVisit:

        for n in range(len(globalWillVisit)):

            i, j = globalWillVisit.popleft()
            matrixBfs[i][j] = meltTime

            for k in range(4):

                ar = dr[k] + i
                ac = dc[k] + j

                if 0 <= ar < r and 0 <= ac < c and (ar, ac) not in footPrints:

                    if matrix[ar][ac] == "X":
                        globalWillVisit.append((ar, ac))
                        footPrints.add((ar, ac))

        meltTime += 1

    return meltTime


def binary_search(min, max, mid):

    #print(min, max)

    if min >= max:
        return

    mid = (min+max) // 2

    #print(mid)

    if possibleMeet([start[0], start[1]], mid):
        #print("y")
        binary_search(min, mid-1, mid)

        global answer
        if answer > mid:
            answer = mid

    else:
        #print("no")
        binary_search(mid+1, max, mid)

def bfs(start, maps, mid, end):
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                visited[ny][nx] = True
                # 백조1이 백조2 위치에 도착할 수 있는 경우
                if ny == end[0] and nx == end[1]:
                    return True
                # 기준 시간초인 mid보다 작은 빙하는 녹아서 이동가능한 것으로 간주
                if maps[ny][nx] <= mid:
                    queue.append((ny, nx))
    return False

r, c = map(int, sys.stdin.readline().split())

matrix = [list(sys.stdin.readline().replace("\n", "")) for _ in range(r)]
matrixBfs = [[0] * c for _ in range(r)]

start = [0, 0]
end = [0, 0]

globalWillVisit = deque()

count = 1


for i in range(r):
    for j in range(c):
        if matrix[i][j] == "L":
            globalWillVisit.append((i, j))
            if count == 1:
                start[0] = i
                start[1] = j
                count += 1

            else:
                end[0] = i
                end[1] = j

        elif matrix[i][j] == ".":
            globalWillVisit.append((i, j))

answer = math.inf

lastTime = updateMatrix()


_min, _max = 0,  lastTime

while _min <= _max:
    mid = (_min + _max) // 2
    if bfs([start[0],start[1]], matrixBfs, mid, [end[0], end[1]]):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1
print(answer)
