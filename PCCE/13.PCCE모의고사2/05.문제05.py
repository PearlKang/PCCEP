# 2     "평년"
# 4     "윤년"
# 100   "평년"
# 400   "윤년"

def solution(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "윤년"
            else:
                return "평년"
        else:
            return "윤년"
    else:
        return "평년"

print(solution(2))
print(solution(4))
print(solution(100))
print(solution(400))