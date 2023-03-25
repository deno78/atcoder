s=input()

if s[0]=="1":
    print("No")
    exit()

c=[0]*7
if s[6]=="1":
    c[0]+=1

if s[3]=="1":
    c[1]+=1

if s[1]=="1":
    c[2]+=1
if s[7]=="1":
    c[2]+=1

if s[0]=="1":
    c[3]+=1
if s[4]=="1":
    c[3]+=1

if s[8]=="1":
    c[4]+=1
if s[2]=="1":
    c[4]+=1

if s[5]=="1":
    c[5]+=1

if s[9]=="1":
    c[6]+=1

for i in range(6):
    for j in range(i+1,7):
        for k in range(j+1,7):
#            print("{}/{}/{}".format(i,j,k))
            if c[i]>0 and c[j]==0 and c[k]>0:
                print("Yes")
                exit()

print("No")




