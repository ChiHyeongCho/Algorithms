
from _collections import deque

n = int(input())

for i in range(n):

    string = input()

    queue = deque()

    for j in string:

        if j == ")" and len(queue) >= 1:
            if queue[len(queue) - 1] == "(":
                queue.reverse()
                queue.popleft()
                queue.reverse()

        else:
            queue.append(j)

    if len(queue) > 0:
        print("NO")

    else:
        print("YES")