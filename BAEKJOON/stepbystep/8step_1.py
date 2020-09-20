A,B,C = map(int,input().split())

# i=1
# while(True):
#     if C*i > A+(B*i) :
#         break
#     i+=1

# print(i)

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))