

def dfs(count, local_answer):

    if count == k:
        answer_set.add(local_answer)
        return

    else:
        for i in range(n):

            if visited[i] == 0:
                visited[i] = 1
                dfs(count+1, local_answer+str(matrix[i]))
                visited[i] = 0


n = int(input())
k = int(input())

matrix = []

for i in range(n):

    matrix += [int(input())]

visited = [0] * n

answer_set = set()

dfs(0, "")

#print(answer_set)

print(len(answer_set))