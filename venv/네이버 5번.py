def solution(dataSource, tags):

    answer = []

    for i in range(len(dataSource)):

        num = 0

        for j in range(len(tags)):
            for k in range(len(dataSource[i])):
                if tags[j] == dataSource[i][k]:

                    num += 1

        dataSource[i] += [num]

    dataSource.sort(key = lambda x : x[len(x)-1], reverse= True)
    print(dataSource)

    for i in range(len(dataSource)):
        if dataSource[i][len(dataSource[i])-1] > 0:
            answer += [dataSource[i][0]]

    return answer


print(solution([
    ["doc1", "t1", "t2", "t3","t4", "t10"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
],
["t1", "t2", "t3", "t4"]
))