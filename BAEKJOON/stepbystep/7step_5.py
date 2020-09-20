word = input()
new_word = word.lower()

w=list(set(new_word))

result=[]
for i in w:
    result.append(new_word.count(i))

for i in result:
    if result.count(i)>1:
        print("?")
        break
    else:
        print(max(result))
        break
    

