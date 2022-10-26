def solution(num_list):
    count_even=0
    answer=[]

    for num in num_list:
        if num%2==0:
            answer.append("even")
            count_even+=1

            if count_even==3:
                break
        else:
            answer.append("odd")

    return answer

print(solution([1,2,6,7,4,3]))
print(solution([4,8,1,2,6,4]))
print(solution([1,2,3,4,5]))