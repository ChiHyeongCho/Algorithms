
from collections import deque
import math

def solution(s):

    # 문제 정의
    answer = math.inf
    string = s


    # 문제 풀이

    if len(s) == 1:
        return 1

    for i in range(1, len(string)//2+1):

        queue = deque()
        answerString = ""
        localString = ""

        # 중복 문자열 갯수
        count = 1

        # 첫 단위 queue 삽입
        queue.append((string[0 : i]))


        # 문자열 Index

        for j in range(i, len(string)+i, i):

            if j == len(string):

                if count > 1:
                    answerString += str(count) + queue.popleft()

                else:
                    answerString += queue.popleft()

                break


            if string[j : j+i] == queue[0]:
                count+=1

            else:

                localString = queue.popleft()

                if count > 1:
                    answerString += str(count) + localString

                else:
                    answerString += localString

                count = 1
                queue.append((string[j : j+i]))


        if answer > len(answerString):
            answer = len(answerString)


    return answer
