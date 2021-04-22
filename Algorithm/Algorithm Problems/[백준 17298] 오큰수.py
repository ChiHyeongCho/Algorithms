
from _collections import deque
import sys

n = int(input())

matrix = list(map(int, sys.stdin.readline().split()))
answerMatrix = [-1 for _ in range(n)]

stack = deque()

for i in range(len(matrix)):

    if len(stack) != 0:

        while matrix[stack[-1]] < matrix[i]:
            answerMatrix[stack.pop()] = matrix[i]

            if len(stack) == 0:
                break

    stack.append(i)



for i in answerMatrix:
    print(i, end = " ")

