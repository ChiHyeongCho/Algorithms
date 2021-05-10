
import heapq

n = int(input())
answer_list = []

for _ in range(n):
    heapq.heappush(answer_list, int(input()))


if n == 1:
    print(0)

else:

    answer = 0
    while len(answer_list) > 1:

        a = heapq.heappop(answer_list)
        b = heapq.heappop(answer_list)

        answer += a + b
        heapq.heappush(answer_list, a+b)

    print(answer)