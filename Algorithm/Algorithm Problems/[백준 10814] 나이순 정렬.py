
from queue import PriorityQueue

n = int(input())
matrix = []
queue = PriorityQueue()

for i in range(n):

    a, b = input().split()

    queue.put(((int(a), i), b))

for i in range(queue.qsize()):

    (a,order), c = queue.get()

    print(a, c)

