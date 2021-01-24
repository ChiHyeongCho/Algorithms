from itertools import product

def solution(user_id, banned_id):

    combination = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):

        len_ban = len(banned_id[i])
        count_star = banned_id[i].count("*")

        for j in range(len(user_id)):

            len_user = len(user_id[j])
            con = 0

            if len_ban == len_user:

                for k in range(len(user_id[j])):
                    if user_id[j][k] == banned_id[i][k]:
                        con += 1

                if con + count_star == len_ban:
                    combination[i] += [user_id[j]]

    answer_set = set()
    a = list(set((product(*combination))))
    ma = len(a[0])

    for i in range(len(a)):

        a[i] = set(a[i])
        if len(a[i]) == ma:
            answer_set.add(tuple(a[i]))
    print(answer_set)
    answer = len(answer_set)

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))