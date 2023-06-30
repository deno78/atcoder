n,l=map(int,input().split())

s=[]
for i in range(n):
    s.append(input())


s.sort()

ans=[]
for c in s:
    ans.append(c)

print("".join(ans))