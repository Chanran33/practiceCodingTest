#문제가 뼈때리네

C = int(input())

result_list=[]
for i in range(C):
    N = list(map(int,input().split()))
    
    avg = sum(N[1:])/N[0]#평균 구하기

    count = 0
    for j in N[1:]:
        if j>avg:
            count+=1
    
    result = round((count/N[0])*100,3)
    result_list.append(result)

for i in result_list:
    print(str("%.3f" % i)+"%")


