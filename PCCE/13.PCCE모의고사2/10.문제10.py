def solution(n,board,position):
    answer=[]
    cnt=0

    direction=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

    for pos in position:
        for dir in direction:
            if pos[0]+dir[0]<0 or pos[1]+dir[1]<0 or pos[0]+dir[0]>len(board)-1 or pos[1]+dir[1]>len(board[0])-1:
                continue

            if board[pos[0]+dir[0]][pos[1]+dir[1]]==1:
                cnt+=1
        
        if board[pos[0]][pos[1]]==0:
            if cnt==2:
                answer.append(1)
            else:
                answer.append(0)
        else:
            if cnt<=2 or cnt>=5:
                answer.append(0)
            else:
                answer.append(1)

        cnt=0

    return answer

# [0]
print(solution(1,[[0,0,0],[0,0,0],[0,0,0]],[[1,1]]))

# [1,0]
print(solution(2,[[0,1,0,0],[1,1,1,0],[0,1,0,1],[0,1,0,1],[1,1,1,0],[0,0,0,1]],[[1,3],[5,3]]))


# dir=[
#     [1,0],
#     [1,1],
#     [0,1],
#     [-1,1],
#     [-1,0],
#     [-1,-1],
#     [0,-1],
#     [1,-1],
# ]

# print(dir[0][1])


# board=[[1,1,1],[1,1,1],[1,1,1]]

# board.insert(0,0)
# board.append(0)

# print(board)

def solution2(n,board,position):
    answer=[]

    for i in range(n):
        x=position[i][0]
        y=position[i][1]
        neighbor=0

        if x!=0:
            # 왼쪽 위
            if y!=0:
                if board[x-1][y-1]:
                    neighbor+=1
            #  위
            if board[x-1][y]:
                neighbor+=1
            # 오른쪽 위
            if y!=len(board[0])-1:
                if board[x-1][y+1]:
                    neighbor+=1
        # 왼쪽
        if y!=0:
            if board[x][y-1]:
                neighbor+=1
        # 오른쪽
        if y!=len(board[0])-1:
            if board[x][y+1]:
                neighbor+=1
        if x!=len(board)-1:
            # 왼쪽 아래
            if y!=0:
                if board[x+1][y-1]:
                    neighbor+=1
            # 아래
            if board[x+1][y]:
                neighbor+=1
            # 오른쪽 아래
            if y!=len(board[0])-1:
                if board[x+1][y+1]:
                    neighbor+=1
        
        if board[x][y]:
            if 3<=neighbor<=4:
                answer.append(1)
            else:
                answer.append(0)
        else:
            if neighbor==2:
                answer.append(1)
            else:
                answer.append(0)

    return answer

# [0]
print(solution2(1,[[0,0,0],[0,0,0],[0,0,0]],[[1,1]]))

# [1,0]
print(solution2(2,[[0,1,0,0],[1,1,1,0],[0,1,0,1],[0,1,0,1],[1,1,1,0],[0,0,0,1]],[[1,3],[5,3]]))