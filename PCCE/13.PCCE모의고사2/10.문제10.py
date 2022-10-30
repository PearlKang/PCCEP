def solution(n,board,position):
    answer=[]
    cnt=0

    direction=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

    for pos in position:
        for dir in direction:
            if pos[0]+dir[0]<0 or pos[1]+dir[1]<0 or pos[0]+dir[0]>len(board)-1 or pos[1]+dir[1]>len(board[0])-1 :
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
