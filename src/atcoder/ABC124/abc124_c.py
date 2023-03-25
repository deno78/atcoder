s=list(map(int,list(input())))
ans=[0]*2
for i in [0,1]:
    for j in range(len(s)):
        if s[j]!=(j+i)%2:
            ans[i]+=1

print(min(ans))
