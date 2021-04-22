
from collections import deque
import sys

n = int(input())
matrix = list(map(int, sys.stdin.readline().split()))
indexMatrix = []
queue = deque()

for i in range(n):
    indexMatrix += [[i, matrix[i]]]

top = 0

for i in range(n):

    while queue:

        if queue[-1][1] > indexMatrix[i][1]:
            print(queue[-1][0]+1, end = " ")
            break

        else:
            queue.reverse()
            queue.popleft()
            queue.reverse()

    if not queue:
        print(0, end = " ")

    queue.append((indexMatrix[i][0], indexMatrix[i][1]))





