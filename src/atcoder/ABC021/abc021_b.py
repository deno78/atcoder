n=int(input())
a,b=map(int,input().split())
k=int(input())
plist=list(map(int,input().split()))

plist.append(a)
plist.append(b)
if len(plist)!=len(list(set(plist))):
    print("NO")
else:
    print("YES")