

n, k = map(int, input().split())

matrix= [i+1 for i in range(n)]
answer_matrix = []

index = 0

while matrix:

    index += k - 1
    index %= len(matrix)

    answer_matrix += [matrix[index]]
    del matrix[index]

    if not matrix:
        break

print("<", end = "")

for i in range(len(answer_matrix)):

    print(answer_matrix[i], end = "")

    if i != len(answer_matrix) - 1:
        print(",", end = " ")

print(">")