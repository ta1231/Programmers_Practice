board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
stack = []
sum = 0
for i in range(len(moves)):
    moves[i] = moves[i] - 1
for i in moves: 
    for j in range(0, len(board)):
        if board[j][i] != 0:
            stack.append(board[j][i])
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop(-1)
                stack.pop(-1)
                sum += 2
            board[j][i] = 0
            break

print(stack)
print(sum)
