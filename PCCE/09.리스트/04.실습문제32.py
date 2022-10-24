# 32
nums=[5,15,2,-8,-12,-29,43,1]

max=-9999
min=9999

for num in nums:
    # print(num)
    if num < min:
        min=num

for num in nums:
    if num > max:
        max=num

print(min,max)