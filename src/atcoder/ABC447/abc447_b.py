s=input()

sdict={}
for c in s:
    if c not in sdict:
        sdict[c]=0
    sdict[c]+=1

m=0
for k,v in sdict.items():
    m=max(m,v)

for k,v in sdict.items():
    if v==m:
        s=s.replace(k,"")

print(s)