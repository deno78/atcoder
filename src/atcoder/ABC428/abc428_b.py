n,k=map(int,input().split())
s=input()

ans1=1
ans2=[]

for i in range(n-k+1):
    w=s[i:i+k]
    wk=1
    for j in range(i+1,n-k+1):
        w2=s[j:j+k]
        if w==w2:
            wk+=1
#    print(i,w,wk)
    if wk>ans1:
        ans1=wk
        ans2=[w]
    elif wk==ans1:
        ans2.append(w)
            
print(ans1)
print(" ".join(sorted(ans2)))