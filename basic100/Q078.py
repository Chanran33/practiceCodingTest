# 반복문 정리
# for문은 반복 횟수가 정해져 있을 때 주로 사용
# while문은 반복 횟수가 정해지지 않은 경우 주로 사용
# range는 연속된 숫자를 생성하는 함수

x = int(input())
result = 0

for i in range(x+1):
    if i%2==0:
        result+=i
    else:
        continue

print(result)