# def sugar(N) :
#     for y in range( (N//3)+1) :
#         for x in range( (N//5)+1 ) :
#             if ((5*x + 3*y) == N) :
#                 return x+y
            
#     return -1

# N = int(input()) #배달해야할 설탕 킬로그램         
# print(sugar(N))

n = int(input())
box = 0

while True:
    if (n % 5) == 0:
        box = box + (n//5)
        print(box)
        break
    n = n - 3   # 안 나눠지면 3킬로그램 배달 수를 하나 늘림
    box += 1    # 배달 수 더해줌    
    if n < 0:
        print('-1')
        break