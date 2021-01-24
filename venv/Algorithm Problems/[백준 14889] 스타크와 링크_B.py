from itertools import combinations

N = int(input()) // 2
M = 2*N
stat = [list(map(int, input().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]
newstat = [i+ j for i, j in zip(row, col)]

print(newstat)

allstat = sum(newstat) // 2
newstat.sort()
newstat[1::2] = newstat[-1::-2]
allstat -= newstat[-1]

mins = 65535
for l in combinations(newstat[:-1], N-1):
    mins = min(mins, abs(allstat - sum(l)))
    if not mins:
        print(0)
        break
else:
    print(mins)