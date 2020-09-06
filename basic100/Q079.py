word = input().split() #word는 리스트!

for i in range(len(word)):
    if(word[i]=='q'):
        print(word[i])
        break
    else:
        print(word[i])