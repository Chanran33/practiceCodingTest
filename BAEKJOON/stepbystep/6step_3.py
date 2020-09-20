def find_Hansu(n):
    hansu=0
    for i in range(1,n+1):
        if i>=1 and i<=99:
            hansu+=1
        else:
            num=[]
            for j in str(i):
                num.append(int(j)) 

            if (num[0]-num[1]) == (num[1]-num[2]):
                hansu+=1
    print(hansu)

x=int(input())
find_Hansu(x)


        

