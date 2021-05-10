
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    matrix = []
    answer = 0

    for i in range(n):
        a, b = map(int, input().split())
        matrix += [[a, b]]

    matrix.sort(key = lambda x : (x[0], x[1]))

    min_score = 200000

    for i in range(len(matrix)-1):

        if matrix[i][0] < matrix[i+1][0]:

            min_score = matrix[i][1]

            if min_score < matrix[i+1][1]:
                answer += 1


    print(n-answer)










