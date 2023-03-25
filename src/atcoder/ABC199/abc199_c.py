n=int(input())
s=list(input())
q=int(input())
s1=s[:n]
s2=s[n:]

iss1=True
for i in range(q):
    tab=list(map(int,input().split()))
    t=tab[0]
    if t==1:
        a=tab[1]-1
        b=tab[2]-1
        if iss1:
            if a<n and b<n:
                c=s1[b]
                s1[b]=s1[a]
                s1[a]=c
            elif a<n and b>=n:
                c=s2[b-n]
                s2[b-n]=s1[a]
                s1[a]=c
            elif a>=n and b<n:
                c=s1[b]
                s1[b]=s2[a-n]
                s2[a-n]=c
            elif a>=n and b>=n:
                c=s2[b-n]
                s2[b-n]=s2[a-n]
                s2[a-n]=c
        else:
            if a<n and b<n:
                c=s2[b]
                s2[b]=s2[a]
                s2[a]=c
            elif a<n and b>=n:
                c=s1[b-n]
                s1[b-n]=s2[a]
                s2[a]=c
            elif a>=n and b<n:
                c=s2[b]
                s2[b]=s1[a-n]
                s1[a-n]=c
            elif a>=n and b>=n:
                c=s1[b-n]
                s1[b-n]=s1[a-n]
                s1[a-n]=c
    elif t==2:
        iss1 = not iss1

if iss1:
    print("".join(s1+s2))
else:
    print("".join(s2+s1 ))
