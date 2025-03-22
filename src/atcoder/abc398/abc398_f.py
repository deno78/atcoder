s=input()

if len(s)==1:
    print(s)
    exit()



l=len(s)
i1=l
for i in range(1,l):
    s1=s[-1*i:]
    s2=s1[::-1]
#    print("{} {} {}".format(i,s1,s2))
    if s1!=s2:
        break
    i1=-1*i
#print(i1)
s1=s[:i1]
s2=s[i1:]
s3=s1[::-1]
#print(s1)
#print(s2)
#print(s3)
print(s1+s2+s3)
