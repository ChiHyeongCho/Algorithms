from collections import deque

def bfs(x, y):

    queue.append((x,y))
    foot_prints.add((x,y))

    while queue:

        r, c = queue.popleft()

        if r == end[0] and c == end[1]:
            return("happy")

        for ax, ay in convience:

            if (ax, ay) not in foot_prints:
                if abs(ax-r) + abs(ay-c) <= 1000:

                    queue.append((ax, ay))
                    foot_prints.add((ax,ay))

    return("sad")





Test = int(input())

for _ in range(Test):

    n = int(input())

    start = list(map(int, input().split()))
    convience = [list(map(int, input().split())) for _ in range(n+1)]
    end = convience[n]

    foot_prints = set()
    queue = deque()
    print(bfs(start[0], start[1]))