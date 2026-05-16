s=input()

wk=[]
for i in range(len(s)):
    if s[i]=="C":
        wk.append(i)

ans=0
for w in wk:
    ans += min(w, len(s) - 1 - w)+1
    

print(ans)