

string = input()
stringlen = len(string)

# 문제풀이

for i in range(stringlen, 2, -1):

    localStringLen = i
    certify = set()
    defi = 0

    for j in range(stringlen - i):

        localString = string[j:i+j]
        certify.add(localString)
        defi += 1


    if len(certify) != defi:
        print(i)
        break


