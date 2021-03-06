x = int(input())
print('%X' % x)

# 파이썬 문자열 서식 지정자에 대하여
# 파이썬은 다양한 방법으로 문자열을 만들 수 있다. 
# 그 중 서식지정자로 문자열을 만드는 방법과
# format 메서드로 문자열을 만드는 문자열 포매팅이 있다.

# 서식지정자로 문자열 넣기
# '%s' % '문자열' : 'I am %s.' % 'james' -> 'I am james'
# 서식지정자로 소수점 표현하기
# '%f' % 숫자 : '%f' % 2.3 -> '2.300000'
# 소수점 이하 자릿수를 지정하기
# '%.자릿수f' % 숫자 : '%.3f' % 2.3 -> '2.300'
# 서식 지정자로 문자열 정렬하기
# %길이s : '%10s' % 'python' -> '    python'

#나머지 내용은 이부분 참고 
#https://dojang.io/mod/page/view.php?id=2300