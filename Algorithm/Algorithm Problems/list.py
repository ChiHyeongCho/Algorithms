
4
def rotate_90(m):

    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]

    return ret


print(rotate_90([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))

import itertools


def solution(info, query):
    answer = ""

    stringMatrix = ["cpp", "java", "python", "-"]
    workMatrix = ["backend", "frontend", "-"]
    carrerMatrix = ["junior", "senior", "-"]
    footMatrix = ["chicken", "pizza", "-"]

    combinationsKey = list(itertools.product(stringMatrix, workMatrix, carrerMatrix, footMatrix))
    combinationsKeyMap = dict()

    combinationslist = list()
    querylist = list()

    for i in range(len(info)):

        string = info[i].split(" ")
        score = string[-1]
        string = string[:-1]
        keystring = ""

        for j in range(len(string)):
            keystring += string[j]

        combinationslist += [[keystring, score]]

    for i in range(len(query)):

        nowQuery = query[i].replace("and", "").replace(" ", "")
        string = info[i].split(" ")
        score = string[-1]
        string = string[:-1]
        keystring = ""

        for j in range(len(string)):
            keystring += string[j]

        combinationslist += [[keystring, score]]

    for i in range(len(combinationsKey)):

        string = ""

        for j in range(len(combinationsKey[i])):
            string += combinationsKey[i][j]

        combinationsKeyMap[string] = 0

    for i in range(len(info)):

        string = info[i].split(" ")
        string = string[:-1]
        keystring = ""

        for j in range(len(string)):
            keystring += string[j]

        combinationsKeyMap[keystring] += 1

    for i in range(len(query)):
        nowQuery = query[i].replace("and", "").replace(" ", "")

        combinationsKeyMap[nowQuery]

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))