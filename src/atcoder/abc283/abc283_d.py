s=input()

box=[]
kakko=[]
sz=0
for i in range(len(s)):
    c=s[i]
    if c=="(":
        kakko.append(sz)
    elif c==")":
        start=kakko.pop()
        for j in range(sz-start):
            box.pop()
        sz=0
    else:
        if c in box:
            print("No")
            exit()
        else:
            box.append(c)
            sz+=1
#    print("[{}]{} box:{}({})".format(i,c,box,sz))
print("Yes")

