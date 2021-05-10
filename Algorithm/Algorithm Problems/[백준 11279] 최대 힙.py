import sys
import heapq

n = int(input())

matrix = []
heap = []


for i in range(n):

    now = int(sys.stdin.readline())
    #print(heap, now, len(heap))


    if now == 0:

        if len(heap) == 0:
            print(0)

        else:
            a, b =heapq.heappop(heap)
            print(b)

    else:
        heapq.heappush(heap, (-now, now))





