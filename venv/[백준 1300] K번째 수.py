

#def findSol(N, K):

N = int(input())
#K = int(input())

answer = 0

for i in range(1, N):

    answer = (i+1)*(i+1)

    side = 0

    for j in range(N-i-1, 0, -1):

        side += j

    answer += 2*side
    print(side)
    print(answer)


#findSol(N, K)


