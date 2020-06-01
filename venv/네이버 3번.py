def solution(road, n):

    answer = 0

    for i in range(len(road)):

        if answer > len(road)-i-1:
            break

        local = 0
        count = n

        for j in range(i, len(road)):

            if road[j] == "0":
                count -= 1

                if count < 0:
                    break
                else:
                    local += 1

            else:
                local += 1

        print(local, count)
        if local > answer:

            answer = local

    return answer

print(solution("111011110011111011111100011111", 3))