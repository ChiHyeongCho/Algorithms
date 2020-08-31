
from collections import deque


def bfs(i):

    answer = 0

    queue = deque()
    footPrints = set()

    queue.append(i)
    footPrints.add(i)

    while queue:

        for k in range(len(queue)):

            ni = queue.popleft()

            if ni == K:
                return answer

            if ni + 1 <= 100000 and (ni + 1) not in footPrints :
                queue.append(ni + 1)
                footPrints.add(ni + 1)
                pathList[ni + 1] = ni

            if ni - 1 >= 0 and (ni-1) not in footPrints:
                queue.append(ni - 1)
                footPrints.add(ni - 1)
                pathList[ni - 1] = ni

            if ni * 2 <= 100000 and (ni * 2) not in footPrints:
                queue.append(2 * ni)
                footPrints.add(2 * ni)
                pathList[2 * ni] = ni

        answer += 1




N, K = map(int, input().split())
pathList = [0]*100001
answerNum = 0
answerPath = [K]

# 문제풀이\



answerNum = bfs(N)

for i in range(answerNum):

    nowPath = answerPath[i]

    answerPath += [pathList[nowPath]]



# 정답출력

print(answerNum)

for i in range(len(answerPath)):

    print(answerPath[len(answerPath) - i - 1], end = " ")



