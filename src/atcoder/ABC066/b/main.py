def chk(m):
    if len(m)%2==1:
        return False
    else:
        ln=len(m)//2
        m1=m[:ln]
        m2=m[ln:]
#        print("{}/{}".format(m1,m2))
        return m1==m2

s=input()

l=len(s)
for i in range(1,l):
    s2=s[:l-i]
    if chk(s2):
        print(l-i)
        exit()
