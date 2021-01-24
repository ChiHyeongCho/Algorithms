
from collections import deque


def solution(ball, order):
    answer = []

    ballQueue = deque()
    ballMap = dict()

    for i in range(len(ball)):

        ballMap[order[i]] = i

    order.sort()

    for i in range(len(ball)):

        ballQueue.append(ball[i])


    while ballQueue:


        if ballMap[ballQueue[0]] > ballMap[ballQueue[len(ballQueue)-1]]:
            ballQueue.reverse()
            n = ballQueue.popleft()
            ballQueue.reverse()
            answer += [n]

        else:
            n = ballQueue.popleft()
            answer += [n]

    return answer


print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]	))