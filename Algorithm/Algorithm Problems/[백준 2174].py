
class robot:

    def __init__(self, c, r, dic, id):

        self.r = r
        self.c = c
        self.dic = dic
        self.id = id


def tr(r):

    return R+1-r


def commandL(robot, reps):

    dir = robot.dic
    d = 0
    if dir == 'N':
        d = 0
    elif dir == 'W':
        d = 1
    elif dir == 'S':
        d = 2
    elif dir == 'E':
        d = 3

    robot.dic = dicL[(d + reps%4)%4]


def commandR(robot, reps):
    dir = robot.dic
    d = 0
    if dir == 'N':
        d = 0
    elif dir == 'E':
        d = 1
    elif dir == 'S':
        d = 2
    elif dir == 'W':
        d = 3

    robot.dic = dicR[(d + reps % 4) % 4]

def check(ar, ac):

    if 1 <= ar <= R and 1 <= ac <= C:
        return True
    else:
        return False


def commandF(robot, reps):

    dir = robot.dic
    d = 0
    if dir == 'N':
        d = 0
    elif dir == 'W':
        d = 1
    elif dir == 'S':
        d = 2
    elif dir == 'E':
        d = 3

    ar = robot.r
    ac = robot.c

    for i in range(reps):

        ar += dr[d]
        ac += dc[d]

        if not check(tr(ar), ac):
            print("Robot %d crashes into the wall" %(robot.id))
            return False

        if Map[tr(ar)][ac] != 0:
            print("Robot %d crashes into robot %d" %(robot.id, Map[tr(ar)][ac]))
            return False

    Map[tr(robot.r)][robot.c] = 0

    robot.r = ar
    robot.c = ac
    Map[tr(ar)][ac] = robot.id
    return True

C, R = map(int, input().split())
N, M = map(int, input(). split())

robots = []*N

Map = [[0]*(C+1) for _ in range(R+1)]

for i in range(N):

    c, r, dic = input().split()
    c = int(c)
    r = int(r)
    robots += [robot(c, r, dic, i+1)]
    Map[tr(r)][c] = i+1


dicL = ['N', 'W', 'S', 'E']
dicR = ['N', 'E', 'S', 'W']

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

sa = True

for i in range(M):

    id, command, reps = input().split()
    id = int(id)
    reps = int(reps)
    id = id - 1

    if command =="L":
        commandL(robots[id], reps)

    elif command == "R":
        commandR(robots[id], reps)

    elif command == "F":
        if not commandF(robots[id], reps):
            sa = False
            break

if sa:
    print("OK")









