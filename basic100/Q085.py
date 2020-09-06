h,b,c,s = map(int,input().split())

result = (h*b*c*s)/(2**23)
print(round(result,1),"MB")
