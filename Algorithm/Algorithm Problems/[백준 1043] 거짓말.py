
def find(a):

    if parent[a] == a:
        return a

    else:
        parent[a] = find(parent[a])
        return parent[a]


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


n, m = map(int, input().split())

temp = list(map(int, input().split()))
truePeople = set()
answer = 0

if len(temp) > 1:

    parent = [i for i in range(n+1)]
    rank = [0 for i in range(n+1)]

    for i in temp[1:]:
        truePeople.add(i)

    for i in range(1, len(temp[1:])):
        union(temp[i], temp[i+1])

    partyPeople = []

    for i in range(m):
        tempParty = list(map(int, input().split()))

        if len(tempParty) <= 1:
            partyPeople += [[]]

        else:
            partyPeople += [tempParty[1:]]

    for i in range(len(partyPeople)):
        for j in range(len(partyPeople[i])-1):

            union(partyPeople[i][j], partyPeople[i][j+1])

    rootNode = parent[temp[1]]

    #print(rootNode)
    #print(parent)

    for i in range(n+1):

        if find(parent[i]) == find(temp[1]):
            truePeople.add(i)

    #print(truePeople)

    for i in range(len(partyPeople)):

        state = True

        for j in range(len(partyPeople[i])):

            if partyPeople[i][j] in truePeople:
                state = False
                break

        if state == True:
            answer += 1


    #print(truePeople)
    #print(partyPeople)
    print(answer)

else:

    for i in range(m):
        tempParty = list(map(int, input().split()))

    print(m)
