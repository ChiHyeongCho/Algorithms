
from queue import PriorityQueue

n, m = map(int, input().split())

link = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
pqueue = PriorityQueue()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        pqueue.put((i, i))

while pqueue.qsize() != 0:

    value, problemNo = pqueue.get()

    answer += [problemNo]

    for i in link[problemNo]:
        indegree[i] -= 1

        if indegree[i] == 0:
            pqueue.put((i, i))

for i in answer:
    print(i, end=' ')






