x,y,z=map(int,input().split())

for i in range(1,10000):
    if y*z==x:
        print("Yes")
        exit()
    x+=1
    y+=1

print("No")