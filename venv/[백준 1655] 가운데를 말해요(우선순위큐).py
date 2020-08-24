
import heapq

Max, Min = [], []

n = int(input())

for _ in range(n):

    number = int(input())

    if len(Max) == len(Min):

        heapq.heappush(Max, (-number, number))

    else:
        heapq.heappush(Min, (number, number))


    if len(Min) > 0 and Min[0][1] < Max[0][1]:

        a = heapq.heappop(Min)[1]
        b = heapq.heappop(Max)[1]

        heapq.heappush(Min, (b, b))
        heapq.heappush(Max, (-a, a))

    print(Max[0][1])