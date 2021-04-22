
from itertools import combinations

def solution(relation):

    colLen = len(relation[0])
    rowLen = len(relation)
    answer = 0
    combinationsMatrix = []
    candidateKey = set()


    for i in range(colLen):
        combinationsMatrix += [i]

    for i in range(colLen):
        certifySet = set()

        for j in range(rowLen):

            certifySet.add(relation[j][i])

        if len(certifySet) == rowLen:
            candidateKey.add(i)
            answer += 1

    for i in range(2, colLen):

        combinationKey = list(combinations(combinationsMatrix, i))

        for j in range(len(combinationKey)):

            certifySet = set()

            for k in range(rowLen):

                addString = ""

                for m in range(len(combinationKey[j])):

                    addString += relation[k][combinationKey[j][m]]

                certifySet.add(addString)

            state = True

            candidateKey = list(candidateKey)

            if len(certifySet) == rowLen:

                for k in range(len(candidateKey)):

                    if (k in list(combinations(combinationKey[j], k))):
                        state = False
                        break

                candidateKey = set(candidateKey)

                if state == True:

                    candidateKey.add(combinationKey[j])
                    answer += 1

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))