
n = input()

matrix = ['']  * len(n)

for i in range(len(n)):

    matrix[i] = n[i]

matrix.sort(reverse = True)

for i in matrix:
    print(i, end = "")