
from collections import deque

class node:

    def __init__(self, name, child):
        self.child = []
        self.name = name

    def addChild(self, anotherNode):
        self.child += [anotherNode]

    def printChild(self):
        return print(self.child)



def bfs(n, link):

    queue = deque()
    queue.append(n)
    footPrints = set()
    footPrints.add(n)

    while queue:

        childNum = 0

        for i in range(len(queue)):

            next = queue.popleft()

            nextVists = nodeDic[next].child

            for j in range(len(nextVists)):

                if nextVists[j] not in footPrints:
                    queue.append(nextVists[j])
                    footPrints.add(nextVists[j])
                    childNum += 1

        link += [childNum]

n = int(input())
nodeDic = dict()

link = []

for i in range(n):

    nodeDic[i+1] = node(i+1, [])


for i in range(n-1):

    start, end = map(int, input().split())
    nodeDic[start].addChild(end)
    nodeDic[end].addChild(start)


bfs(1, link)

answerOne = 0
answerTwo = 0

for i in range(len(link)):
    if i%2 == 1:
        answerOne += link[i]

    else:
        answerTwo += link[i]

print(min(answerOne, answerTwo))