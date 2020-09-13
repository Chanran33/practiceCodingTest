n=int(input()) #10
numbers=list(map(int,input().split())) #1 3 2 2 5 6 7 4 5 9
a=list() #빈 리스트 

#0으로 초기화
for i in range(23): # 0~22
    a.append(0)

for i in numbers:
    a[i-1]=a[i-1]+1

for i in range(23):
    print(a[i], end=' ')


# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(1,24):
#     print(arr.count(i))