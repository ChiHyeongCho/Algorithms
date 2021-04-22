
n, m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dpMatrix = [[0] * (sum(cost)+1) for _ in range(n+1)]

for i in range(sum(cost)+1):

    for j in range(1, n+1):

        if i < cost[j-1]:
            dpMatrix[j][i] = dpMatrix[j-1][i]

        else:

            dpMatrix[j][i] = max(dpMatrix[j-1][i], memory[j-1] + dpMatrix[j-1][i-cost[j-1]])

answer = sum(cost)+1

for i in range(sum(cost)+1):

    for j in range(1, n+1):

        if dpMatrix[j][i] >= m and i < answer:
            answer = i

print(answer)

#for i in range(n+1):

#    print(dpMatrix[i])