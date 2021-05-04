
import heapq
import math

answer = []

n = int(input())
for i in range(n):

    numbers = list(map(int, input().split()))

    for j in numbers:

        heapq.heappush(answer, j)

        if len(answer) > n:
            heapq.heappop(answer)

print(answer[0])

