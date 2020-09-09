
from collections import deque


def checkRight(string):

    queue = deque()
    stringLen = len(string)


    for i in range(stringLen):


        if  len(queue) != 0:

            if queue[len(queue)-1] == "(" and string[i] == ")":
                queue.reverse()
                queue.popleft()
                queue.reverse()
                continue
            else:
                queue.append(string[i])
                continue

        else:
            queue.append(string[i])


    if len(queue) > 0:
        return False
    else:
        return True


def checkequal(string):

    if string.count('(') == string.count(')'):
        return True
    else:
        return False


def recursion(string, answer):

    u = ""
    v = ""

    if len(string) == 0:
        return ""

    for i in range(len(string)):

        u = string[0 : i+1]
        v = string[i+1 : len(string)]

        if checkequal(u) == True and checkequal(v) == True:
            break


    if checkRight(u) == True:

        return u + recursion(v, answer)

    else:

        localAnswer = "("
        localAnswer += recursion(v, answer)
        localAnswer += ")"

        newU = u[1:len(u)-1]

        for i in range(len(newU)):

            if newU[i] == "(":
                localAnswer += ")"

            else:
                localAnswer += "("


        answer += localAnswer

    return answer



def solution(p):

    # 문제 변수 정의

    answer = ""

    # 올바른 괄호 문자열 체크

    if len(p) == 0 or checkRight(p) == True:
        answer = p

    else:
        answer = recursion(p, "")


    return answer


print(solution("()))((()"))

