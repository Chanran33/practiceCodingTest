# X=int(input())

# #멀라 어케 풀어
# line=1
# while X>line:
#     X-=line
#     line+=1
    
# if line%2==0:
#     a=X
#     b=line-X+1
# else:
#     a=line-X+1
#     b=X
    
# print(a, '/', b, sep='')


# x = int(input())
# count = 0   # 누적 
# plus = 1    # 각각 묶여지는 값 (1, 2~3, 4~6, 7~10)
# m = 1
# n = 1

# while True:
#     count += plus
#     if x <= count:
#         y = count - x
#         if plus % 2 == 0:
#             print(m + (plus-1) - y,n + y, sep='/')
#             break
#         else:
#             print(m + y,n + (plus -1) - y, sep='/')
#             break
#     plus +=1

X = int(input())

#X가 몇번째 대각선인지 찾아보자!
line = 1
line_sum = 0
pre_line_sum = 0
while True:
    pre_line_sum = line_sum
    line_sum+=line
    
    if line_sum >= X :
        break

    line+=1

X_num = X-pre_line_sum #X가 대각선 라인에서 몇번째에 위치하는지 찾아봄!
rev_X_num = line_sum+1-X

if line%2==0 :
    print(X_num,rev_X_num,sep="/") 
else :
    print(rev_X_num,X_num,sep="/")

#47분 걸림