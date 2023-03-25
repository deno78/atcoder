# TODO edit the code

# param
s=list(input())

# solve

ans=0
for c in list("atcoder"):
    i1="atcoder".index(c)
    i2=s.index(c)
    while i1!=i2:
        i2=s.index(c)
        fw=1
        if i1 < i2:
            fw=-1
        elif i1 == i2:
            break
        st=s[i2+fw]
        s[i2+fw]=s[i2]
        s[i2]=st
        ans+=1

print(ans)
