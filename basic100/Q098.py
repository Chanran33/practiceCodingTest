a, b = map(int, input().split())

board=[]

#보드값 초기화
for i in range(a):
    line =[]
    for j in range(b):
        line.append(0)
    board.append(line)

#막대 개수 
bar = int(input())

#막대 저장
bars =[]
for i in range(bar): #0,1,2
    b = list(map(int, input().split())) #[2,0,1,1]
    bars.append(b) #[[2,0,1,1], [3,1,2,3], [4,1,2,5]]

#바꿔 보자!
for i in range(bar): #0,1,2
   for j in range(bars[i][0]): #2,3,4
        if bars[i][1]==0:
            if(board[bars[i][2]-1][bars[i][3]-1+j]==0):
                board[bars[i][2]-1][bars[i][3]-1+j]=1
            else:
                board[bars[i][2]-1][bars[i][3]-1+j]=0
        else:
            if(board[bars[i][2]-1+j][bars[i][3]-1]==0):
                board[bars[i][2]-1+j][bars[i][3]-1]=1
            else:
                board[bars[i][2]-1+j][bars[i][3]-1]=0

       
#결과 출력
for i in board:
    for j in i:
        print(j, end=' ')
    print()
