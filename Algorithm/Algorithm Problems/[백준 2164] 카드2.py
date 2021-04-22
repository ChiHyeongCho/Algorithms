from collections import deque

N = int(input())
queue = deque()

for i in range(N):

    queue.append(i)


while True:

    if len(queue) == 1:

        print(queue.popleft()+1)
        break


    queue.popleft()

    shuffle = queue.popleft()
    queue.append(shuffle)




