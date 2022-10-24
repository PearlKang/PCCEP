# 기본 함수 형태
def add_num(a,b):
    res=a+b
    return res

# 결과값이 없는 함수
def div_num(a,b):
    res=a/b
    print("나눗셈 결과",res)

# 매개변수가 없는 함수
import random

def get_random_number():
    res=random.randint(1,100)
    return res

# 결과값, 매개변수가 없는 함수
def say_hello():
    print("안녕하세용!")
    print("반갑습니당!")

print(add_num(10,20))
div_num(10,20)
print(get_random_number())
say_hello()