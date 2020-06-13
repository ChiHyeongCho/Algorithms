
from itertools import combinations
import math

t = int(input())

for _ in range(t):

    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]

    x_all = 0
    y_all = 0

    answer = math.inf

    for i in range(n):

        x_all += matrix[i][0]
        y_all += matrix[i][1]


    indi = list(combinations(matrix, n//2))

    for i in range(len(indi)):

        x_split = 0
        y_split = 0

        for j in range(len(indi[i])):

            x_split += indi[i][j][0]
            y_split += indi[i][j][1]

        local_answer = math.sqrt((2*x_split-x_all)**2 + (2*y_split-y_all)**2)

        if local_answer < answer:

            answer = local_answer

    print('%7f' %answer)