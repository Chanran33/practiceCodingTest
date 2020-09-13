n = int(input()) #10
numbers = list(map(int,input().split()))

min = numbers[0]

for i in range(1,n):#1~9
    if numbers[i]<=min:
        min = numbers[i]
    
print(min)
