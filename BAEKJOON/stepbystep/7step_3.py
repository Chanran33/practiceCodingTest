s=input()

print(*list(map(s.find,map(chr,range(97,123)))))

#map은 리스트의 요소를 지정된 함수로 처리해주는 함수
#map은 원본 리스트를 변경하지 않고 새 리스트를 생성
#list(map(함수,리스트))