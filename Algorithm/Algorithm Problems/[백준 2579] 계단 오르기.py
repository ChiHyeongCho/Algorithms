
n = int(input())
steps = []

for i in range(n):

    steps += [int(input())]


dp_matrix = [0 for _ in range(n)]

if n == 0:
    print(0)

elif n == 1:
    dp_matrix[0] = steps[0]

elif n == 2:
    dp_matrix[0] = steps[0]
    dp_matrix[1] = steps[0] + steps[1]

else:

    dp_matrix[0] = steps[0]
    dp_matrix[1] = steps[0] + steps[1]
    dp_matrix[2] = max(steps[0] + steps[2],
                       steps[1] + steps[2])

    for i in range(3, n):

        dp_matrix[i] = max(steps[i] + steps[i-1] + dp_matrix[i-3],
                           steps[i] + dp_matrix[i-2])


#print(dp_matrix)
if n > 0:
    print(dp_matrix[n-1])
