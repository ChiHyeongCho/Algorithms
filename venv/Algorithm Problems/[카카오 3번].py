import itertools

def solution(info, query):

    answer = []

    combinationslist = list()
    querylist = list()

    for i in range(len(info)):

        string = info[i].split(" ")
        score = string[-1]
        string = string[:-1]

        stringMatrix = [string[0], "-"]
        workMatrix = [string[1], "-"]
        carrerMatrix = [string[2],  "-"]
        footMatrix = [string[3],  "-"]

        combinationsKey = list(itertools.product(stringMatrix, workMatrix, carrerMatrix, footMatrix))

        for j in range(len(combinationsKey)):

            keystring = ""

            for k in range(len(combinationsKey[j])):

                keystring += combinationsKey[j][k]

            combinationslist += [[keystring, score]]


    for i in range(len(query)):

        string = query[i].replace("and", "")
        string = string.split(" ")

        score = string[-1]
        string = string[:-1]
        keystring = ""

        for j in range(len(string)):
            keystring += string[j]

        querylist += [[keystring, score]]


    for i in range(len(querylist)):

        localAnswer = 0

        for j in range(len(combinationslist)):

            if querylist[i][0] == combinationslist[j][0] and int(querylist[i][1]) <= int(combinationslist[j][1]):

                localAnswer += 1

        answer += [localAnswer]



    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))