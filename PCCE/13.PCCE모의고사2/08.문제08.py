def solution(num_list):
    for n in range(0,len(num_list)):
        for i in range(0,len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                num_list[i],num_list[i+1]=num_list[i+1],num_list[i]

    return num_list

print(solution([2,4,3,1]))

def solution2(num_list):
    for n in range(len(num_list)-1):
        for i in range(len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                num_list[i],num_list[i+1]=num_list[i+1],num_list[i]

    return num_list

print(solution2([2,4,3,1]))

def solution3(num_list):
    for n in range(len(num_list)-1):
        for i in range(len(num_list)-1-n):
            if num_list[i]>num_list[i+1]:
                num_list[i],num_list[i+1]=num_list[i+1],num_list[i]

    return num_list

print(solution3([2,4,3,1]))
