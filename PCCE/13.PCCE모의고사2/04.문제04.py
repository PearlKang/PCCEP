# 1 1
# 3 6
# 5 120

n=int(input())

factorial=1

for i in range(1,n+1):
    factorial*=i

print(factorial)

factorial=1

for i in range(n):
    factorial*=i+1

print(factorial)