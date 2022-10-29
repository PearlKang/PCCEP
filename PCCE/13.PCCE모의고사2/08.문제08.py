def solution(num_list):
    for n in range(0,len(num_list)):
        for i in range(0,len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                num_list[i],num_list[i+1]=num_list[i+1],num_list[i]

    return num_list

print(solution([2,4,3,1]))