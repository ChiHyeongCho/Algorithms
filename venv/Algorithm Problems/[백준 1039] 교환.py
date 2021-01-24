
import copy
from itertools import combinations
from collections import deque

def bfs(stringN):

    answer = 0
    count = 0

    queue = deque()
    queue.append(stringN)
    answerList = []

    while queue:

        footPrints = set()

        if count == k+1:
            return max(answerList)

        for m in range(len(queue)):

            x = queue.popleft()

            # print(x, count)

            if count == k:
                answerList += [int(x)]

            for i in range(len(combinationList)):

                xList = list(x)
                start, end = combinationList[i]

                if x[end] == "0" and start == 0:
                    continue

                else:
                    xList[start], xList[end] = xList[end], xList[start]
                    nextString = ""

                    for j in range(len(xList)):
                        nextString += xList[j]


                    if nextString not in footPrints:
                        footPrints.add(nextString)
                        queue.append(nextString)

        count += 1

    return answer

n, k = map(int, input().split())

stringN = str(n)
matrix = []

for i in range(len(stringN)):
    matrix += [i]

combinationList = list(combinations(matrix, 2))

globalAnswer = bfs(stringN)

if globalAnswer == 0:
    print(-1)
else:
    print(globalAnswer)



