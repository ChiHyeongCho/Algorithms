
import copy

def solution(n, weak, dist):

    # 문제 정의

    answer = 10
    dist.reverse()
    dist.sort(reverse = True)

    # 문제 풀이 (그리디 알고리즘)

    # 시작점
    for i in range(len(weak)):

        # 방향 설정
        for j in [-1, 1]:

            footPrints = [0]*len(weak)
            curWeakIndex = i
            curPoint = weak[i]


            # 길이가 긴 것부터 탐색
            for k in range(len(dist)):

                footPrints[curWeakIndex] = 1
                curWeakIndex += j

                for _ in range(dist[k]):

                    curPoint += j

                    if curPoint >= n:
                        curPoint = 0

                    if curPoint < 0:
                        curPoint = n-1

                    if curWeakIndex >= len(weak):
                        curWeakIndex = 0

                    if curWeakIndex < 0:
                        curWeakIndex = len(weak)-1


                    if curPoint == weak[curWeakIndex]:

                        footPrints[curWeakIndex] = 1
                        curWeakIndex += j

                if 0 not in footPrints:
                    if answer > k+1:
                        answer = k+1


                if curWeakIndex >= len(weak):
                    curWeakIndex = 0

                if curWeakIndex < 0:
                    curWeakIndex = len(weak) - 1

                curPoint = weak[curWeakIndex]


    if answer == 10:
        return -1
    else:
        return answer


print(solution(200,  [0, 100], [1,1]))

print(solution(200,  [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))

print(solution(50,  [1], [6]))