# 34
import random

lotto_num=[] # 로또 번호 리스트
count=0 # 뽑은 로또 번호 갯수

while True:
    num=random.randint(1,45)
    
    if num not in lotto_num:
        lotto_num.append(num)
        count+=1
        if count==6:
            break

print(lotto_num)

for lotto in lotto_num:
    print(lotto,end=" ")

lotto_num=[]

while True:
    if len(lotto_num)==6:
        break

    num=random.randint(1,45)
    
    if num not in lotto_num:
        lotto_num.append(num)

print(lotto_num)