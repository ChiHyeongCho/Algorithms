
import sys

from _collections import deque

t = int(sys.stdin.readline())

for i in range(t):

    order = sys.stdin.readline()

    n = int(sys.stdin.readline())

    queue = deque()
    matrix_raw = sys.stdin.readline()[1:-1].split(",")
    state = True


    for j in matrix_raw:
        if j != "":
            queue.append(j)

    for j in order:

        if j == "R":
            queue.reverse()

        elif j == "D":

            if len(queue) == 0:
                state = False
                break

            else:
                queue.popleft()

    if state == False:
        print("error")

    else:
        answer = "["

        while queue:

            answer += queue.popleft()

            if len(queue) != 0:
                answer += ","

        answer += "]"

        print(answer)