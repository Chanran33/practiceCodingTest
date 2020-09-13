n = int(input())
white = list() #흰바둑돌 위치 저장할 빈 리스트 생성
for i in range(n):
    x = list(map(int, input().split()))
    white.append(x)


baduk = []

#19X19판에 0으로 초기화
for i in range(19):
    line=[]
    for j in range(19):
        line.append(0)
    baduk.append(line)

#흰 바둑돌 놓기
for x,y in white:
    baduk[x-1][y-1]=1

#19X19판 출력
for i in baduk:
    for j in i:
        print(j, end=' ')
    print()