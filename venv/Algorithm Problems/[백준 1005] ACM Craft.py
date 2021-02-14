import sys
from _collections import deque

t = int(sys.stdin.readline())

for _ in range(t):

    n, k = map(int, sys.stdin.readline().split())
    bulidTime = list(map(int, sys.stdin.readline().split()))

    nextVisits = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    queue = deque()
    dpMatrix = [0 for _ in range(n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        nextVisits[a-1].append(b-1)
        indegree[b-1] += 1

    w = int(sys.stdin.readline()) - 1


    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            dpMatrix[i] = bulidTime[i]

    answer = 0
    answerList = []

    while queue:

        nowPoint = queue.popleft()
        answerList += [nowPoint]

        for k in nextVisits[nowPoint]:
            indegree[k] -= 1
            dpMatrix[k] = max(dpMatrix[nowPoint] + bulidTime[k], dpMatrix[k])

            if indegree[k] == 0:
                queue.append(k)

    #print(dpMatrix)
    print(dpMatrix[w])
    #print(answerList)