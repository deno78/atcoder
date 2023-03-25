# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans=0

for l in range(len(s)):
    wk=[True]*10
    c1=int(s[l])
    wk[c1]=False
    for r in range(l+1,len(s)):
        c2=int(s[r])
        wk[c2]= not wk[c2]
        if wk[0] and wk[1] and wk[2] and wk[3] and wk[4] and wk[5] and wk[6] and wk[7] and wk[8] and wk[9]:
            ans+=1
            
# answer
print(ans)
