from queue import PriorityQueue
import math

def dijkstra(start, n, graph):

    distance = [math.inf] * n

    queue = PriorityQueue
    queue.put(0, start)

    while queue.qsize() != 0:

        dist, now = queue.get()

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                queue.put(cost, i[0])
