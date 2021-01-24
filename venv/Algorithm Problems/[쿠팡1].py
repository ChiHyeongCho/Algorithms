answerlist = [0, 0]

for n in range(2, 10):

    number = 14
    localAnswer = ""

    while number // n >= 1:
        remain = number % n
        number = number // n
        localAnswer = str(remain) + localAnswer
        if number < n :
            localAnswer = str(number) + localAnswer

    local = 1

    for i in range(len(localAnswer)):
        if int(localAnswer[i]) != 0:
            local *= int(localAnswer[i])

    if local >= answerlist[1]:
        answerlist[0] = n
        answerlist[1] = local

    print(n, local)

print(answerlist)