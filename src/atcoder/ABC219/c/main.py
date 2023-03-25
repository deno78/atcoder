x=list(input())
abc="abcdefghijklmnopqrstuvwxyz"

xdic={}
for i in range(26):
    c1=abc[i]
    c2=x[i]
    xdic[c2]=c1
trans=str.maketrans(xdic)

n=int(input())
slist=[]
sdic={}
for i in range(n):
    name=input()
    name2=name.translate(trans)
    sdic[name2]=name

for k,v in sorted(sdic.items(),key=lambda x:x[0]):
    print(v)

