

def solution(food_times, k):

    lessTime = k
    totalFoodTime = sum(food_times)

    totalNumberFood = len(food_times)
    emptyFood = 0
    emptyFoodSet = set()

    numberOfIter = 0

    while True:

        if lessTime <= totalFoodTime-emptyFood:
            break


        lessTime -= totalFoodTime - emptyFood


    answer = 0
    return answer


print(solution([3, 1, 2], 5))