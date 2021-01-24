
def sum(N):

    Sum = 0

    start = 1
    digit = 1

    while True:

        if start > N:
            break

        end = start*10 - 1

        if end > N:
            end = N

        Sum += digit * (end-start+1)

        digit += 1
        start *= 10

    return Sum






N, K = map(int, input().split())

determin = sum(N)

if determin < K:
    print(-1)

else:


    start, end = 1, N

    while True:

        mid = (start+end)//2

        deter = sum(mid)

        if deter - len(str(mid)) + 1 <= K <= deter:

            print(str(mid)[len(str(mid))-deter+K-1])
            break

        elif deter < K:

            start = mid

        else:

            end = mid
