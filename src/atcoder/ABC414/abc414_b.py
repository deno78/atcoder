n=int(input())
cl=[]
for i in range(n):
    wk=input().split()
    c=wk[0]
    l=int(wk[1])
    cl.append((c,l))

s=[]
for c,l in cl:
    if l>100:
        print("Too Long")
        exit()
    s.extend([c]*l)
    if len(s)>100:
        print("Too Long")
        exit()

if len(s)>100:
    print("Too Long")
else:
    print("".join(s))