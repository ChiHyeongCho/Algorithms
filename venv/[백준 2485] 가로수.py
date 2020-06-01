
N = int(input())

trees = [0]*N

for i in range(N):

    trees[i] = int(input())

trees = sorted(trees)

Min = 100000000

for i in range(N-1):

    local = trees[i+1] - trees[i]

    if local < Min:

        Min = local

case = []

start = Min

while True:

    case.append(Min)

    if Min == 1:
        break

    else:

        if Min%2 == 1:
            break

        else:

            Min = Min//2

for i in range(len(case)):

    state = True
    contrast = set()
    next = trees[0]

    while True:

        contrast.add(next)

        if next >= trees[len(trees)-1]:
            break

        else:

            next += case[i]

    for j in range(N):

       if trees[j] not in contrast:
           state = False
           break

    print(contrast)

    if state:
        print(contrast)
        print(len(contrast)-len(trees))
        break


