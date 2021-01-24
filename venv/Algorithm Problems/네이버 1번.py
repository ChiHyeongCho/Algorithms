
def solution(boxes):

    number = [0]*(1000001)
    answer = 0

    for i in range(len(boxes)):

        number[boxes[i][0]] += 1
        number[boxes[i][1]] += 1

    for i in range(len(number)):

        if number[i]%2 == 1 and number[i] > 0 :
            answer += 1

    return answer//2



print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))