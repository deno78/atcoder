# TODO edit the code

# param
s = input()
t = input()

# solve
s2=[]
t2=[]
p=""
con=False


p=s[0]
l=0
for i in range(len(s)):
    c = s[i]    
    if p == c:
        l+=1
    else:
        s2.append([p,l])
        p=c
        l=1
s2.append([p,l])

p=t[0]
l=0
for i in range(len(t)):
    c = t[i]    
    if p == c:
        l+=1
    else:
        t2.append([p,l])
        p=c
        l=1
t2.append([p,l])

if len(s2) != len(t2):
    print("No")
    exit()
else:
    for i in range(len(s2)):
        sc = s2[i]
        tc = t2[i]
        if sc[0] != tc[0]:
            print("No")
            exit()
        else:
            if sc[1] ==1 and tc[1] !=1:
                print("No")
                exit()
            if sc[1] !=1 and tc[1] ==1:
                print("No")
                exit()
            if sc[1] > tc[1]:
                print("No")
                exit()

print("Yes")