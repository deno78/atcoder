n,q=map(int,input().split())

sv=[]
pc=[]
ans=0
for i in range(n):
    pc.append([])

for i in range(q):
    query=input().split()
    idx=int(query[1])-1
    if query[0]=="1":
        pc[idx]=[sv]
    elif query[0]=="2":
        s=query[2]
        pc[idx].append(s)
    elif query[0]=="3":
        sv="".join(pc[idx])

print(sv)