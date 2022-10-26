def solution(num_list):
    answer=[]
    cnt=0

    for num in num_list:
        for i in range(1,num+1):
            if num%i==0:
                cnt+=1

        if cnt==2:
            answer.append(True)
        else:
            answer.append(False)

        cnt=0
    
    return answer

print(solution([2,3,4,5,6,7,8,9]))