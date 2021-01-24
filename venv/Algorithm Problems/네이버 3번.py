

import math

Min = math.inf
temp = [0]*2

def perm(string, step):

    global Min

    if(len(string) == 1):

        if step < Min:
            Min = step
            temp[0] = step
            temp[1] = int(string)

        return

    for i in range(1, len(string)):

        a = string[0:i]
        b = string[i : len(string)+1]

        if len(b) > 1 and b[0] == "0":
            continue

        start = int(a)
        end = int(b)

        sum = str(start + end)


        perm(sum, step+1)


def solution(n):

    nString = str(n)

    perm(nString, 0)

    answer = [temp[0], temp[1]]

    return answer

print(solution(10007))