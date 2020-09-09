
def binarySearch(left, right):

    middle = (left+right)//2


    global answer

    if left > middle:

        answer = middle
        return


    if K <= check(middle):

        binarySearch(middle+1, right)

    else:

        binarySearch(left, middle-1)



def check(num):

    local = 0

    for i in range(N):
        local += lenLine[i] // num

    return local



# 문제정의

N, K = map(int, input().split())

lenLine = [int(input()) for _ in range(N)]

# 문제풀이 - 이진탐색

answer = 0

left = 1
right = max(lenLine)

binarySearch(left, right)

print(answer)