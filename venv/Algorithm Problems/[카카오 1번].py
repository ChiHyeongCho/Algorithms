
from collections import deque

def solution(new_id):

    step1 = new_id.lower()
    answer = ""

    #print(step1)

    possibeMatrix = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                     "-", "_", "."]

    step2 = ""

    for i in range(len(step1)):

        if step1[i] in possibeMatrix or step1[i].isdigit():
            step2 += step1[i]

    #print(step2)

    step3 = ""
    step3Queue = deque()

    for i in range(len(step2)):

        step3Queue.append(step2[i])

    while step3Queue:

        appendStr = step3Queue.popleft()

        if len(step3) == 0:
           step3 += appendStr

        else:
            if appendStr == ".":
                if appendStr != step3[-1]:
                    step3 += appendStr

            else:
                step3 += appendStr

    #print(step3)

    step4 = step3

    if step3[0] == ".":
        step4 = step4[1:]

    if step3[-1] == ".":
        step4 = step4[:-1]

    #print(step4)

    step5 = ""

    if len(step4) == 0:
        step5 = "a"

    else:
        step5 = step4

    #print(step5)

    step6 = ""

    if len(step5) >= 16:

        step6 = step5[0:15]
        if step6[len(step6)-1] == ".":
            step6 = step6[0:14]


    else:

        step6 = step5

    #print(step6)

    step7 = step6

    while True:

        if len(step7) >= 3:
            break

        else:
            step7 += step7[len(step7)-1]


    answer = step7

    return answer


print(solution(	"abcdefghijklmn.p"))