
def dfs(answer, length):

    global globalState

    if n == len(answer):
        globalState = True
        print(answer)
        return answer

    for i in stringArray:

        if globalState == True:
            return

        localAnswer = answer

        localAnswer += i
        state = True

        for j in range(1, len(localAnswer)//2+1):
                if localAnswer[-j:] == localAnswer[-2*j:-j]:
                    state = False

        if state:
            dfs(localAnswer, length+1)


        else:
            continue

    return

n = int(input())

stringArray = ["1", "2", "3"]
answer = "1"
globalState = False

dfs(answer, 0)
