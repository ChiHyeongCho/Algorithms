
import sys
sys.setrecursionlimit(100000)

def dfs(start):

    for i in arr[start]:

        if parent[i] == 0:
            #visited.add(i)
            parent[i] = start
            dfs(i)
            #visited.remove(i)
    return

n = int(input())

parent = [0 for i in range(n+1)]
arr = {i:[] for i in range(1,n+1)}

for i in range(n-1):

    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


visited = set()
visited.add(1)
parent[1] = 1

dfs(1)

for i in range(2, len(parent)):

    print(parent[i])