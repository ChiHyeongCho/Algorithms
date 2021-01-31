
from itertools import combinations
from collections import deque

def solution(orders, course):

    answer = []

    menuName = set()

    for i in range(len(orders)):

        for j in range(len(orders[i])):

            menuName.add(orders[i][j])

    menuName = list(menuName)
    menuName.sort()


    for i in course:

        combinationMenu = list(combinations(menuName, i))
        combinationMenuIndex = [0, 0]*len(combinationMenu)


        for j in range(len(combinationMenu)):

            combinationMenuIndex[j] = [combinationMenu[j], 0]

        max = 1
        maxlist = deque()


        for j in range(len(combinationMenu)):

            for k in range(len(orders)):

                count = 0

                for m in range(len(combinationMenu[j])):

                    if combinationMenu[j][m] in orders[k]:
                        count += 1

                    else:
                        break

                if count == len(combinationMenu[j]):
                    combinationMenuIndex[j][1] += 1

            if combinationMenuIndex[j][1] > max:
                maxlist = deque()
                maxlist.append(list(combinationMenuIndex[j][0]))
                max = combinationMenuIndex[j][1]

            elif combinationMenuIndex[j][1] == max and max != 1:
                maxlist.append(list(combinationMenuIndex[j][0]))

        answer += maxlist

    # 정렬

    answerList = [0] * len(answer)

    for i in range(len(answer)):

        string = ""

        for j in range(len(answer[i])):

            string += answer[i][j]

        answerList[i] = string

    answerList.sort()

    return answerList

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))