
import sys
import math
from queue import PriorityQueue


def dijkstra(start, graph):

    distanceMatrix = [math.inf] * n
    countSet = set()

    queue = PriorityQueue()
    queue.put((0, start))

    while queue.qsize() != 0:

        dist, now = queue.get()
        countSet.add(now)

        if distanceMatrix[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distanceMatrix[i[0]]:
                distanceMatrix[i[0]] = cost
                queue.put((cost, i[0]))

    answerTime = 0

    for i in distanceMatrix:
        if i != math.inf:
            if answerTime < i:
                answerTime = i

    return len(countSet), answerTime


t = int(input())

for _ in range(t):

    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b-1] += [[a-1, s]]

    a, b = dijkstra(c-1, graph)

    print(a, b)

