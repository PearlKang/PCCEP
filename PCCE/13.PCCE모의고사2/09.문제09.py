def solution(serial):
    answer = []
    
    gender=serial[:2]
    dept=serial[2:4]
    team=str(int(serial[4:6]))
    valid_num=int(serial[6:])
    valid_num_chk=0
    
    for i in range(6):
        valid_num_chk+=int(serial[i])
    
    if gender=="01":
        answer.append("male")
    elif gender=="02":
        answer.append("female")
    
    if dept=="10":
        answer.append("operation")
    elif dept=="11":
        answer.append("sales")
    elif dept=="12":
        answer.append("develop")
    elif dept=="13":
        answer.append("finance")
    elif dept=="14":
        answer.append("law")
    elif dept=="15":
        answer.append("research")
    
    answer.append(team+"team")
    
    if valid_num_chk%13==valid_num:
        answer.append("valid")
    elif valid_num_chk%13!=valid_num:
        answer.append("invalid")
    
    return "/".join(answer)

print(solution("01100103"))
print(solution("02131003"))