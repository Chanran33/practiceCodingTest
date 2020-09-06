# a = input()

# b = ord(a)
# i = ord('a')

# while i<=b:
#     print(chr(i), end=' ')
#     i+=1


char = ord(input())
a = ord('a')


for i in range(a, char+1):
    print(chr(i))
    a = a+1