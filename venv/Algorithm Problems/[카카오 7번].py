
def find(i):

    if (i == parent[i]):
        return i

    parent[i] = find(parent[i])

    return parent[i]


def union(i, j):

    i = find(i)
    j = find(j)

    if i == j:
        return

    if level[i] > level[j]:

        level[j] += level[i]
        parent[i] = j

    else:

        level[i] += level[j]
        parent[j] = i


    return

parent = [0] * 1000
level = [1] * 1000

def solution(sales, links):

    number = len(sales)

    answer = 0


    for i in range(len(links)):

        union(links[i][0]-1, links[i][1]-1)

    for i in range(len(sales)):

        print(find[i])

    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))