
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

    elif rank[x] < rank[y]:
        parent[x] = y
        rank[y] += 1

    else:
        parent[y] = x
        rank[x] += 1

    return


n, m, k = map(int, input().split())
friendMoneyList = list(map(int, input().split()))
friendLink = list(list(map(int, input().split())) for _ in range(m))


usingMoney = 0
answerDict = {i : [] for i in range(1, n+1)}

parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

for i in friendLink:

    a, b = i

    union(a, b)

for i in range(1, len(parent)):

    parent[i] = find(parent[i])
    answerDict[parent[i]] += [friendMoneyList[i-1]]

for i in range(1, n+1):

    if len(answerDict[i]) != 0:
        usingMoney += min(answerDict[i])

#print(answerDict)

if usingMoney > k:
    print("Oh no")

else:
    print(usingMoney)