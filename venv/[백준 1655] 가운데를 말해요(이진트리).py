
def sort():

    numbersLen = len(numbers)
    lower = 0
    upper = numbersLen-2

    if numbersLen == 1:
        return

    if numbersLen == 2:

        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return

    if numbers[numbersLen-2] <= numbers[numbersLen-1]:
        return

    if numbers[0] >= numbers[numbersLen-1]:
        temp = numbers[numbersLen-1]
        numbers[1:numbersLen] = numbers[0:numbersLen-1]
        numbers[0] = temp
        return

    while True:

        middle = (lower + upper) // 2

        if lower == middle:
            temp = numbers[numbersLen-1]
            numbers[middle+1 : numbersLen] = numbers[middle : numbersLen-1]
            numbers[middle+1] = temp
            break

        elif numbers[middle] <= numbers[numbersLen-1]:
            lower = middle

        else:
            upper = middle


N = int(input())

numbers = []

for i in range(N):

    numbers += [int(input())]

    sort()

    if len(numbers)%2 == 1:
        print(numbers[int(len(numbers)/2)])

    else:
        denominator = len(numbers)//2 - 1
        print(min(numbers[denominator], numbers[denominator+1]))
