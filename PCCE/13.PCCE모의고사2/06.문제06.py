def solution(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

print(solution(5))

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()