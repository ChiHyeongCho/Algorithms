def solution(k, room_number):

    answer = []
    check = [0]*(k+1)

    for i in range(len(room_number)):
        if check[room_number[i]] == 0:
            check[room_number[i]] = i+1

        else:
            for j in range(room_number[i], k+1):
                if check[j] == 0:
                    check[j] = i+1
                    break

        answer += [check.index(i+1)]

    return answer
