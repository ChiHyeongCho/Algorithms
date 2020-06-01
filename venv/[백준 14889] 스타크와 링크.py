from collections import deque
from itertools import combinations

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

player = [0]*N

for i in range(N):

    player[i] = i


combi = list(combinations(player, N//2))

middle = len(combi)//2

start_player = combi[:middle]
link_player = list(reversed(combi[middle:]))

region = 100*20

for i in range(len(start_player)):

    foot_print = set()

    start = 0
    link = 0

    local_start = start_player[i]
    local_link = link_player[i]

    for j in range(len(local_start)):
        for k in range(len(local_start)):


            if j != k:
                start += matrix[local_start[j]][local_start[k]]

    for j in range(len(local_link)):
        for k in range(len(local_link)):


            if j != k:
                link += matrix[local_link[j]][local_link[k]]

    local = abs(start-link)

    if local < region:

        region = local

print(region)
