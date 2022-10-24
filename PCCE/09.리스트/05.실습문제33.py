# 33
nums=[5,15,2,-8,-12,-29,43,1]

i=1
sum=0

for num in nums:
    if i%2==1:
        sum+=num
    i+=1

print(sum)

sum=0

for num in nums[::2]:
    sum+=num

print(sum)

