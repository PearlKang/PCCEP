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

def solution2(serial):
    answer=""
    gender=serial[:2]
    part=serial[2:4]
    team=serial[4:6]
    vnum=serial[6:]

    # 성별
    if gender=="01":
        answer+="male"
    elif gender=="02":
        answer+="female"
    answer+="/"

    # 소속 부서
    if part=="10":
        answer+="operation"
    elif part=="11":
        answer+="sales"
    elif part=="12":
        answer+="develop"
    elif part=="13":
        answer+="finance"
    elif part=="14":
        answer+="law"
    elif part=="15":
        answer+="research"
    answer+="/"

    # 소속 팀
    answer+=str(int(team))+"team"
    answer+="/"

    # 유효성 번호
    check_sum=0
    for n in serial[:6]:
        check_sum+=int(n)
    
    if check_sum%13==int(vnum):
        answer+="valid"
    else:
        answer+="invalid"

    return answer

print(solution2("01100103"))
print(solution2("02131003"))

def solution3(serial):
    answer=""
    gender=serial[:2]
    part=serial[2:4]
    team=serial[4:6]
    vnum=serial[6:]

    info={
        "01":"male",
        "02":"female",
        "10":"operation",
        "11":"sales",
        "12":"develop",
        "13":"finance",
        "14":"law",
        "15":"research"
    }
    # 성별
    answer+=info[gender]
    answer+="/"

    # 소속 부서
    answer+=info[part]
    answer+="/"

    # 소속 팀
    answer+=str(int(team))+"team"
    answer+="/"

    # 유효성 번호
    check_sum=0
    for n in serial[:6]:
        check_sum+=int(n)
    
    if check_sum%13==int(vnum):
        answer+="valid"
    else:
        answer+="invalid"

    return answer

print(solution3("01100103"))
print(solution3("02131003"))