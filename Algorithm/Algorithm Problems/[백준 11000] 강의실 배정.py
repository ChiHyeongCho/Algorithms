
import heapq
import sys

n = int(input())
matrix = []

for i in range(n):

    a, b = map(int, sys.stdin.readline().split())
    matrix += [[a, b]]

matrix.sort(key = lambda x : x[0])


heap = []

heapq.heappush(heap, matrix[0][1])

for i in range(1, len(matrix)):

    if heap[0] > matrix[i][0]:

        heapq.heappush(heap, matrix[i][1])

    else:

        heapq.heappop(heap)
        heapq.heappush(heap, matrix[i][1])

print(len(heap))

