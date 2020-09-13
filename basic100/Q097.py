baduk=[] #빈 바둑판 생성
change=[] #바꿀 좌표값 저장

#바둑판 초기값 입력받기
for i in range(19):#0~18
    line = list(map(int, input().split()))
    baduk.append(line)

#바둑판 좌표 개수 입력받기
n=int(input())

#바둑판 바꿀 좌표 입력받기
for i in range(n):
    x = list(map(int, input().split()))
    change.append(x)#change=[[10,10],[12,12]]

#바둑판 바꾸기-가로줄
for x in range(n):
    for i in range(19):
        if baduk[change[x][0]-1][i]==0 :
            baduk[change[x][0]-1][i]=1
        else :
            baduk[change[x][0]-1][i]=0

#바둑판 바꾸기-세로줄        
for x in range(n):
    for i in range(19):
        if baduk[i][change[x][1]-1]==0 :
            baduk[i][change[x][1]-1]=1
        else :
            baduk[i][change[x][1]-1]=0


#바둑판 출력
for i in baduk:
    for j in i:
        print(j, end=' ')
    print()

#n = int(input())

#a=[[0 for i in range(19)] for j in range(19)]

#for s in range(n):
#   x,y = map(int,input().split())
#    a[x-1][y-1] = 1

#for i in range(19):
#   for j in range(19):
#        print(a[i][j], end=' ')
#    print()

#arr = [[0]*19 for i in range(19)]
#for i in range(19):
#    arr[i] = list(map(int, input().split()))

#n = int(input())

#def flip(a):
#    if a==1 : return 0
#    else : return 1


#for i in range(n):
#    x, y = map(int, input().split())
#    for j in range(19):
#        arr[x-1][j] = flip(arr[x-1][j])
#    for k in range(19):
#        arr[k][y-1] = flip(arr[k][y-1])

#for i in arr:
#    for j in i:
#        print(j, end=' ')
#    print()