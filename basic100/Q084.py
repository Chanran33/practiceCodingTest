R,G,B = map(int,input().split())

count = 0

for i in range(R):
    for j in range(G):
        for z in range(B):
            print(i,j,z)
            count+=1

print(count)