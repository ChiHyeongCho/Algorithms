
import math

def solution(n, s, a, b, fares):


    taxiCost = [[100000000 for _ in range(n)] for _ in range(n)]

    for i in range(len(fares)):

        start, end, cost = fares[i]

        taxiCost[start-1][end-1] = min(cost, taxiCost[start-1][end-1])
        taxiCost[end-1][start-1] = taxiCost[start-1][end-1]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    taxiCost[i][j] = 0
                else:
                    taxiCost[i][j] = min(taxiCost[i][j], taxiCost[i][k] + taxiCost[k][j])

    answer = math.inf

    for i in range(n):

        localanswer = taxiCost[a-1][i] + taxiCost[b-1][i] + taxiCost[s-1][i]

        if i == a-1:
            localanswer -= taxiCost[a-1][i]

        if i == b-1:
            localanswer -= taxiCost[b-1][i]

        if i == s-1:
            localanswer -= taxiCost[s-1][i]

        if localanswer < answer:
            answer = localanswer

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))