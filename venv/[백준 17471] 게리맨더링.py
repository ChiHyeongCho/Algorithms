
from collections import deque
import copy


def check(check_foot_prints):

    check_queue = deque()

    for i in range(N):

        if i not in check_foot_prints:

            check_queue.append(i)
            break

    while check_queue:

        i = check_queue.popleft()

        for j in range(N):


            if link_list[i][j] == 1 and j not in check_foot_prints:

                check_queue.append(j)
                check_foot_prints.add(j)


    if len(check_foot_prints) != N:

        return False

    else:

        return True


def dfs(i, local, foot_prints):

    if len(foot_prints) == N:

        return

    global region

    check_foot_prints = copy.deepcopy(foot_prints)

    if len(foot_prints) != 0:

        if check(check_foot_prints):

            local_reverse = All - local

            if abs(local-local_reverse) < region:

                region = abs(local-local_reverse)


    for j in range(N):


        if j not in foot_prints and link_list[i][j] == 1:

            foot_prints.add(j)

            dfs(j, local+population[j], foot_prints)

            foot_prints.remove(j)

    return



N = int(input())

population = list(map(int, input().split()))
link_list = [[0]*N for _ in range(N)]
All = sum(population)

for i in range(N):

    a = input()

    if len(a) > 1:

        information = list(map(int, a.split()))

        if information[0] >= 1:

            for j in range(1, len(information)):

                link_list[i][information[j]-1] = 1
                link_list[information[j]-1][i] = 1


region = 100*100


for i in range(N):

    foot_prints = set()
    foot_prints.add(i)
    dfs(i, population[i], foot_prints)

if region == 100*100:
    print(-1)

else:
    print(region)