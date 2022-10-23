# 26
pilgi=int(input("필기시험 점수를 입력하세요:"))

if pilgi>=80:
    interview=input("면접결과를 입력하세요:")
    
    if interview=="pass":
        print("최종합격")
    elif interview=="fail":
        print("불합격")
else:
    print("불합격")