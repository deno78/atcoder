s=input()
k=int(input())

if k > len(s):
    print(0)
    exit()

ans=[]
for j in range(len(s)-k):
    ans.append(s[j:j+k])

ans=list(set(ans))
#print(ans)
print(len(ans))
