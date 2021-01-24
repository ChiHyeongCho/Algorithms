

Test = int(input())

for i in range(Test):

    Str = list(map(str, input().split()))

    answer = float(Str[0])

    for j in range(1, len(Str)):

        if Str[j] == "@":

            answer *= 3

        elif Str[j] == "%":

            answer += 5

        else:

            answer -= 7

    print(format(answer, ".2f"))
