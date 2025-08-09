s=input()

ans=0
for i1 in range(len(s)-1):
    for i2 in range(i1+1,len(s)):
        if s[i1]=="t" and s[i2]=="t" and (i2-i1)>=2:
            s1=s[i1:i2+1]
            x=s1.count("t")-2
            l=(i2-i1-1)
#            print(i1,i2,s1,x,l)
            w=x/l
            ans=max(ans,w)
        else:
            ans=max(ans,0)
print(ans)
