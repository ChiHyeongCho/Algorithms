from collections import deque

def solution(inputString):

    answer = 0

    Str = inputString

    queue1 = deque()
    queue2 = deque()
    queue3 = deque()
    queue4 = deque()

    for i in range(len(Str)):

        if Str[i] == "(":
            queue1.append(Str[i])

        elif len(queue1) == 0 and Str[i] ==")":
            queue1.append(Str[i])
            break

        elif len(queue1) > 0 and Str[i] == ")" and queue1[len(queue1)-1] == "(":
            queue1.reverse()
            queue1.popleft()
            queue1.reverse()
            answer += 1


        if Str[i] == "{":
            queue2.append(Str[i])

        elif len(queue2) == 0 and Str[i] =="}":
            queue2.append(Str[i])
            break

        elif len(queue2) > 0 and Str[i] == "}" and queue2[len(queue2)-1] == "{":
            queue2.reverse()
            queue2.popleft()
            queue2.reverse()
            answer += 1

        if Str[i] == "[":
            queue3.append(Str[i])

        elif len(queue3) == 0 and Str[i] =="]":
            queue3.append(Str[i])
            break

        elif len(queue3) > 0 and Str[i] == "]" and queue3[len(queue3)-1] == "[":
            queue3.reverse()
            queue3.popleft()
            queue3.reverse()
            answer += 1

        if Str[i] == "<":
            queue4.append(Str[i])

        elif len(queue4) == 0 and Str[i] ==">":
            queue4.append(Str[i])
            break

        elif len(queue4) > 0 and Str[i] == ">" and queue4[len(queue4)-1] == "<":
            queue4.reverse()
            queue4.popleft()
            queue4.reverse()
            answer += 1

    if len(queue1) + len(queue2) + len(queue3) + len(queue4) == 0:
        return answer
    else:
        return -1

print(solution("if([({<as>d}f]d)e)d d(C1o2u3nt of eggs is 4.) {Buy milk.})"))