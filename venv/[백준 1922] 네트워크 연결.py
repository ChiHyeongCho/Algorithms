
def find(i):

    if (i == parent[i]):
        return i

    parent[i] = find(parent[i])

    return parent[i]


def union(i, j, c):

    i = find(i)
    j = find(j)

    if i == j:
        return

    if level[i] > level[j]:

        level[j] += level[i]
        parent[i] = j

    else:

        level[i] += level[j]
        parent[j] = i

    global cost

    cost += c

    return



n = int(input())

m = int(input())

matrix = [list(map(int, input().split())) for _ in range(m)]

index = 0

cost = 0

while True:

    if index == len(matrix) - 1:
        break

    if matrix[index][0] == matrix[index][1]:

        del matrix[index]

    else:

        index += 1


matrix.sort(key = lambda x : x[2])

parent = [0]*n
level = [1]*n

for i in range(n):

    parent[i] = i

for i in range(len(matrix)):

    union(matrix[i][0]-1, matrix[i][1]-1, matrix[i][2])

print(cost)