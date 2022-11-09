def solution(board):
    answer = 0
    cnt=0

    direction=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

    for dir in direction:
        if board[1+dir[0]][1+dir[1]]==1:
            cnt+=1

        if board[1][1]==0:
            if cnt==2:
                answer=1
            else:
                answer=0
        else:
            if cnt<=2 or cnt>=5:
                answer=0
            else:
                answer=1
    
    return answer

print(solution([[0,1,0],[0,1,0],[0,0,1]])) # 0
print(solution([[0,0,0],[0,0,1],[1,0,0]])) # 1
print(solution([[1,1,0],[0,1,1],[1,0,1]])) # 0
print(solution([[1,0,0],[0,1,0],[1,0,1]])) # 1

def solution2(board):
    answer=0
    neighbor=board[0][0]+board[0][1]+board[0][2]+board[1][0]+board[1][2]+board[2][0]+board[2][1]+board[2][2]

    if board[1][1]:
        if 3<=neighbor<=4:
            answer=1
        else:
            answer=0
    else:
        if neighbor==2:
            answer=1
        else:
            answer=0

    return answer

print(solution2([[0,1,0],[0,1,0],[0,0,1]])) # 0
print(solution2([[0,0,0],[0,0,1],[1,0,0]])) # 1
print(solution2([[1,1,0],[0,1,1],[1,0,1]])) # 0
print(solution2([[1,0,0],[0,1,0],[1,0,1]])) # 1