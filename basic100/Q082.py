x = input()

for i in range(1,16):
    print(x,"*",format(i,'X'),"=",format(int(x,16)*i,'X'),sep='')
