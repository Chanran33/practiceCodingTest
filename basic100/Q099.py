
#개미 집 입력 받기
miro = [[0]*10 for i in range(10)]

for i in range(10):
    miro[i] = list(map(int,input().split()))

#개미의 현재 위치
x=1
y=1 

while True:
    if x==8 and y==8:
        miro[x][y]=9
        break
    
    if miro[x][y]==2:
        miro[x][y]=9
        break

    miro[x][y] = 9

    if miro[x][y+1]==1:
        x+=1
    elif miro[x][y+1]==0 or 2:
        y+=1

for i in miro : 
    for j in i:
        print(j, end=' ')
    print()

