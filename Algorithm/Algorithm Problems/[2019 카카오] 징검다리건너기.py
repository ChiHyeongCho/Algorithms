def solution(stones, k):

    blank = []

    answer = 0

    while True:

        for i in range(len(blank)):

            a = blank[i]-1
            b = blank[i]+1

            if 0<=a<len(stones) and 0<= b < len(stones):
                if stones[a] == 0 and stones[b] == 0:
                    return answer
        answer += 1





print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))