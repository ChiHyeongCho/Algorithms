
n = int(input())

matrix = set()

for i in range(n):

    matrix.add(input())

matrix = list(matrix)

matrix.sort()
matrix.sort(key = lambda x:len(x))

for i in range(len(matrix)):

    print(matrix[i])