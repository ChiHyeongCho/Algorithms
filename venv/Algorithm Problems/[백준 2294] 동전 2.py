
# 문제 정의

n, k = map(int, input().split())

coins = []
dp = [-1] * (k+1)

for i in range(n):

    coins += [int(input())]
    if coins[i] <= k:
        dp[coins[i]] = 1

# 문제 풀이

for i in range(2, k+1):

    maxSet = set()

    for j in range(len(coins)):

        if i >= coins[j] and dp[i-coins[j]] != 0:

            if dp[i] == 1:
                maxSet.add(1)
                continue

            if dp[i - coins[j]] != -1:
                maxSet.add(dp[i - coins[j]]+1)


    if len(maxSet) > 0:
        dp[i] = min(maxSet)

    else:
        dp[i] = -1


print(dp[k])
