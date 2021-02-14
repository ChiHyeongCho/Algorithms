
def find(x):

    if x == parent[x]:
        return x


    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):

    x = find(a)
    y = find(b)

    if x == y:
        return

    else:

        if rank[x] < rank[y]:
            parent[x] = y
            rank[y] += 1

        else:
            parent[y] = x
            rank[x] += 1


n = int(input())
m = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
cities = list(map(int, input().split()))

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):

        if matrix[i][j] == 1:
            union(i, j)

answerSet = set()

for i in cities:

    answerSet.add(find(parent[i-1]))

if len(answerSet) == 1:
    print("YES")
else:
    print("NO")