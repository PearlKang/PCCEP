# 조건문
# : 조건에 따라 실행할 명령을 선택하는 것

origin_pass="1234"
input_pass=input("비밀번호 입력:")

if origin_pass==input_pass: # 조건 A
    # 조건 A 참
    print("로그인 성공!")
    print("반갑습니다.")
elif input_pass=="": # 조건 B
    # 조건 A 거짓, 조건 B 참
    print("빈칸을 입력해 주세요.")
else:
    # 조건 A 거짓, 조건 B 거짓
    print("로그인 실패!")
    print("비밀번호가 틀렸습니다.")

print("프로그램 종료")