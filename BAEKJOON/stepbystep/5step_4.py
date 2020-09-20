nums=[]

for i in range(10):
    x = int(input())
    nums.append(x%42)

set_nums=set(nums)

print(len(set_nums))

