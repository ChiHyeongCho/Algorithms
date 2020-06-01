from itertools import combinations


def solution(answer_sheet, sheets):

    cont = list(combinations(sheets, 2))

    answer = 0

    for i in range(len(cont)):

        a = cont[i][0]
        b = cont[i][1]
        check = [0]*len(answer_sheet)

        num = 0
        pro = 1
        ma_pro = 1

        for j in range(len(answer_sheet)):

            if a[j] == b[j] and a[j] != answer_sheet[j]:
                num += 1
                check[j] = 1

            if check[j] == 1:
                if j > 0 and check[j-1] == 1:
                    pro += 1
                    if pro > ma_pro:
                        ma_pro = pro

            else:
                pro = 1

        if num == 0:
            ma_pro = 0

        local = num + ma_pro*ma_pro

        if local > answer:
            answer = local

    return answer


print(solution("111111", ["222222","222222","222222","111111","333333"]))