# 리스트 만들기
company_list=["삼성전자","SK하이닉스","네이버"]

# 데이터 접근하기 (인덱싱)
print(company_list[0])
print(company_list[1])
print(company_list[2])

# 데이터 할당하기
company_list[0]="애플"
company_list[1]="구글"
company_list[2]="테슬라"
print(company_list)

# 데이터 추가하기
company_list.append("아마존")
print(company_list)

# 데이터 삭제하기
del company_list[0]
print(company_list)

# 리스트 길이
print(len(company_list))

# 리스트 슬라이싱
print(company_list[0:2]) # 0,1
print(company_list[:2]) # 처음 안써도 됨
print(company_list[1:3])
print(company_list[1:]) # 마지막 안써도 됨
print(company_list[::2])