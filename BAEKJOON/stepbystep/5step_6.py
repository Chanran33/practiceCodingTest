n = int(input())

result_list=[]
for i in range(n):
    line = input()

    r=0
    result=0

    for j in line:
        if j=='O':
            r+=1
            result+=r
        elif j=='X':
            r=0

    result_list.append(result)
    

for i in result_list:
    print(i)
