n=int(input())
numbers=list(map(int,input().split()))

for i in reversed(numbers):
    print(i, end=' ')