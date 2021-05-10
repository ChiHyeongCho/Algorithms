
from collections import deque

while True:

    string = input()
    queue = deque()

    if string == ".":
          break

    for i in string:

        if i == "[" or i == "]" or i == "(" or i == ")":

            #print(queue)

            if len(queue) == 0:

                queue.append(i)

            else:

                if i == "[":

                    queue.append(i)

                elif i == "]":

                    if queue[-1] == "[":
                        queue.reverse()
                        queue.popleft()
                        queue.reverse()

                    else:
                        queue.append(i)

                elif i == "(":

                    queue.append(i)

                else:

                    if queue[-1] == "(":
                        queue.reverse()
                        queue.popleft()
                        queue.reverse()

                    else:
                        queue.append(i)

    #print(queue)
    if len(queue) == 0:
        print("yes")

    else:
        print("no")

