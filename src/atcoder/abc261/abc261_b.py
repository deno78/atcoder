# TODO edit the code

# param
n = int(input())
amap=[]
for i in range(n):
    amap.append(list(input()))

# solve
for i in range(n):
    for j in range(n):
        if i!=j:
            r1=amap[i][j]
            r2=amap[j][i]
    #        print("{}/{}".format(r1,r2))
            if r1=="W" and r2 != "L":
                print("incorrect")
                exit()
            if r1=="L" and r2 != "W":
                print("incorrect")
                exit()
            if r1=="D" and r2 != "D":
                print("incorrect")
                exit()
            if r2=="W" and r1 != "L":
                print("incorrect")
                exit()
            if r2=="L" and r1 != "W":
                print("incorrect")
                exit()
            if r2=="D" and r1 != "D":
                print("incorrect")
                exit()
            
# answer
print("correct")
