plist=list(map(int,input().split()))

abc="abcdefghijklmnopqrstuvwxyz"

ans=[]
for p in plist:
    ans.append(abc[p-1])

print("".join(ans))