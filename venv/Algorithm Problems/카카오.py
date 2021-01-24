from collections import deque

def solution(board, moves):

    queue = deque()
    answer = 0
    for i in range(len(moves)):

        for r in range(len(board[0][:])):
            if board[r][moves[i]-1] != 0:
                queue.append(board[r][moves[i]-1])
                board[r][moves[i]-1] = 0
                break

        if len(queue) > 1:
            if queue[len(queue)-1] == queue[len(queue)-2]:
                queue.reverse()
                queue.popleft()
                queue.popleft()
                queue.reverse()

                answer += 2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))