def solution(snapshots, transactions):

    answer = [[]]

    Account = []
    for i in range(len(snapshots)):
        Account += [snapshots[i][0]]



    ID = []

    for i in range(len(transactions)):

        if transactions[i][0] not in ID:
            ID += [transactions[i][0]]

            if transactions[i][2] not in Account:
                snapshots += [[transactions[i][2], transactions[i][3]]]
                Account += [transactions[i][2]]

            else:
                if transactions[i][1] == "SAVE":
                    for j in range(len(snapshots)):
                        if snapshots[j][0] == transactions[i][2]:
                            snapshots[j][1] = str(int(snapshots[j][1]) + int(transactions[i][3]))

                else:

                    for j in range(len(snapshots)):
                        if snapshots[j][0] == transactions[i][2]:
                            snapshots[j][1] = str(int(snapshots[j][1]) - int(transactions[i][3]))

        else:
            continue

    snapshots.sort(key = lambda x : x[0])
    answer = snapshots

    return answer



print(solution([
  ["ACCOUNT2", "100"],
  ["ACCOUNT1", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
))