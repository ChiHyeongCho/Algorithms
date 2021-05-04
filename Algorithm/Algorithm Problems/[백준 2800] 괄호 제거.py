
from _collections import deque
from itertools import combinations

str = input()
queue = deque()

pair_index = []
answer_list = set()

for i in range(len(str)):

    if str[i] == "(":

        queue.append((i, str[i]))

    elif str[i] == ")":

        queue.reverse()
        index, char = queue.popleft()
        queue.reverse()

        pair_index += [[index, i]]



combinaiton_list = []


for i in range(1, len(pair_index)+1):

    combinaiton_list += list(combinations(pair_index, i))

for i in range(len(combinaiton_list)):

    index_list = []

    for j in range(len(combinaiton_list[i])):

        index_list += [combinaiton_list[i][j][0]]
        index_list += [combinaiton_list[i][j][1]]

    new_string = ""

    for j in range(len(str)):

        if j in index_list:
            continue

        else:
            new_string += str[j]

    answer_list.add(new_string)



answer_list = list(answer_list)

answer_list.sort()

for i in answer_list:
    print(i)

