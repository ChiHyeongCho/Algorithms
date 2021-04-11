import sys

treeMap = dict()
total = 0

while True:

    name = sys.stdin.readline().rstrip()

    if not name:
        break

    treeMap.setdefault(name, 0)
    treeMap[name] += 1
    total += 1

for name in sorted(treeMap.keys()):
    print('{0} {1:0.4f}'.format(name, treeMap[name]*100/total))


