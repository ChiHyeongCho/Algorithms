
Test = int(input())

for i in range(Test):

    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(M)]

    print(N-1)


