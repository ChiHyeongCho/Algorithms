
from queue import PriorityQueue
import math

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]

for i in range(e):

    s, e, w = map(int, input().split())

    graph[s] += [[e, w]]

distance = [math.inf for _ in range(v+1)]

queue = PriorityQueue()

queue.put((0, start))

while queue.qsize() != 0:

    dist, now = queue.get()

    if distance[now] < dist:
        continue

    for i in graph[now]:

        cost = dist + i[1]

        if cost < distance[i[0]]:

            distance[i[0]] = cost
            queue.put((cost, i[0]))

print(distance)