
n = int(input())

matrix_one = [input() for _ in range(n)]
matrix_two = [input() for _ in range(n)]

order_dic = dict()

answer = 0

for i in range(n):

    order_dic[matrix_one[i]] = i

for i in range(n):
    for j in range(i, n):
        #print(order_dic[matrix_two[i]], order_dic[matrix_two[j]])
        if order_dic[matrix_two[i]] > order_dic[matrix_two[j]]:
            answer += 1
            break


print(answer)

#print(order_dic)