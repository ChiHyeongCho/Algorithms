
from collections import deque


def solution(record):

    answer = []
    queueId = deque()
    queueState = deque()
    mapNickname = dict()


    for i in range(len(record)):

        record[i] = record[i].split()


        if record[i][0] == "Enter":
            queueState.append("님이 들어왔습니다.")
            queueId.append(record[i][1])
            mapNickname[record[i][1]] = record[i][2]


        elif record[i][0] == "Leave":
            queueState.append("님이 나갔습니다.")
            queueId.append(record[i][1])

        else:
            mapNickname[record[i][1]] = record[i][2]



    for i in range(len(queueState)):

        answer += [mapNickname[queueId[i]] + queueState[i]]


    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))