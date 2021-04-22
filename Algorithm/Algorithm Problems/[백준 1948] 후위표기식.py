

from _collections import deque

string = input()
queue = deque()
answerString = ""

for i in string:

    if i == "(":
        queue.append(i)

    elif i == ")":
        queue.reverse()

        while True:
            if queue.popleft() == "(":
                break
            else:
                answerString += queue.popleft()

        queue.reverse()

    elif i == "*" or i == "/":
        queue.popleft()

    elif i == "+" or i == "-":

        if queue[-1] == "*" or queue[-1] == "/":

        pass

    else:
        answerString += i

print(answerString)