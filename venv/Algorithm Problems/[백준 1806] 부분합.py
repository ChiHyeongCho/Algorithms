
import math

N, S = map(int, input().split())
matrix = list(map(int, input().split()))
answer = math.inf

sum = 0
endPoint = 0

state = True

for i in range(N):


    while True:

        if endPoint > len(matrix) - 1:
            break

        if state == True:
            sum += matrix[endPoint]

        if sum >= S:
            #print(i, endPoint, sum)
            sum -= matrix[i]
            state = False

            if endPoint-i < answer:
                answer = endPoint-i

            break

        else:
            endPoint += 1
            state = True

if answer == math.inf:
    print(0)

else:
    print(answer+1)

