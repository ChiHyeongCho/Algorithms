
t = int(input())

for _ in range(t):

    n = int(input())

    dp_matrix = [0] * n


    if n == 1:

        dp_matrix[0] = 1

    elif n == 2:

        dp_matrix[0] = 1
        dp_matrix[1] = 2

    elif n == 3:

        dp_matrix[0] = 1
        dp_matrix[1] = 2
        dp_matrix[2] = 4

    else:

        dp_matrix[0] = 1
        dp_matrix[1] = 2
        dp_matrix[2] = 4

        for i in range(3, n):

            dp_matrix[i] = dp_matrix[i-1] + dp_matrix[i-2] + dp_matrix[i-3]

    print(dp_matrix[n-1])