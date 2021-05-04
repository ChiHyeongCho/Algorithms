
n = int(input())

dp_matrix = [0] * n

if n == 1:
    dp_matrix[0] = 3

elif n == 2:
    dp_matrix[0] = 3
    dp_matrix[1] = 7

else:

    dp_matrix[0] = 3
    dp_matrix[1] = 7

    for i in range(2, n):

        dp_matrix[i] = (dp_matrix[i-1] * 2 + dp_matrix[i-2])%9901




print(dp_matrix[n-1])
