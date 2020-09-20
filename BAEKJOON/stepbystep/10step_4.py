def hanoi(N,A,B,C):
    if N < 2:
        print(A,B) 
        return
    hanoi(N-1,A,C,B) #마지막 원반 제외하고 여유 원반에 나머지 원반 순서대로 놓기
    print(A,B) #목적지 원반에 마지막 원반 넣기
    hanoi(N-1,C,B,A) #나머지 원반들 목적지 원반에 넣기

n=int(input())
print((2**n)-1) #하노이탑 옮긴 횟수는 원반갯수 제곱에 -1이다.
hanoi(n,1,3,2)
