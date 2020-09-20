def Flymeto(d):#함수 정의
    i=1
    while(True):
        if(i**-2)-i < d and (i**2)+i >=d:
            break
        i+=1
    
    if i**2 < d:
        return i+i
    else:
        return i+i-1


T = int(input())
result = []
for i in range(T):
    x,y = map(int,input().split())

    distance = y-x
    result.append(Flymeto(distance))

for i in range(T):
    print(result[i])