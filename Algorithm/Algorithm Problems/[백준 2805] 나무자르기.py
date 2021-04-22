import sys

N, M = map(int, input().split())

trees = list(map(int, sys.stdin.readline().split()))

Max, Min = max(trees), 0

index = (Max+Min)//2

answer = index


while True:

    get = 0

    for i in range(len(trees)):

        if trees[i] - index > 0:

            get += trees[i] - index

    if get > M:

        if index == (index + Min)//2:
            answer = index
            break

        Min = index
        index = (index + Max)//2


    elif get < M:

        Max = index
        index = (index + Min)//2

    else:
        answer = index
        break

print(answer)