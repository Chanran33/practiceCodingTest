nums=[]
for i in range(9):
    x=int(input())
    nums.append(x)

print(max(nums))
print(nums.index(max(nums))+1)

#index()함수 : 배열에서 원하는 값의 위치 찾기 