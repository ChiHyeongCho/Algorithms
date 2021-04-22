
def search(low, high, n):

    if low >= high:
        return low

    mid = (low+high)//2

    if lis[mid] < n:
        return search(mid+1, high, n)

    else:
        return search(low, mid, n)


n = int(input())

matrix = list(map(int, input().split()))

temp = 0

lis = [matrix[0]] + [0] *(n-1)

for i in matrix:

    if lis[temp] < i:
        temp += 1
        lis[temp] = i

    else:
        next_loc = search(0, temp, i)
        lis[next_loc] = i

answer = 0

for i in range(len(matrix)):

    if lis[i] != 0:
        answer += 1

print(answer)