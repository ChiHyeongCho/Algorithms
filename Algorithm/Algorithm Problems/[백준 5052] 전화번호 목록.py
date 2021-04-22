
t = int(input())

for i in range(t):

    n = int(input())

    intMatrix = list()
    stringSet = set()
    state = True

    for j in range(n):

        intMatrix += [(input())]

    intMatrix.sort(key = lambda x:len(x))

    minStringLen = len(str(intMatrix[0]))

    for j in range(n):

        nowString = str(intMatrix[j])

        for k in range(minStringLen, len(nowString)+1):

            if nowString[0 : k] in stringSet:
                state = False
                break

        stringSet.add(nowString)

        if state == False:
            break

    if state == False:
        print("NO")

    else:
        print("YES")





