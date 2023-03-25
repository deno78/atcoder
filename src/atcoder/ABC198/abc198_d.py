import itertools
 
s1=input()
s2=input()
s3=input()
 
s=set(list(s1+s2+s3))
 
alpha=list(s)
nums=list('1234567890')
 
if len(alpha) >10:
    print('UNSOLVABLE')
    exit()
 
for ary in itertools.permutations(nums,len(alpha)):
    f=""
    t=""
    for i in range(len(ary)):
        f=f+alpha[i]
        t=t+ary[i]
    ts=str.maketrans(f,t)
    if (int(s1[-1].translate(ts))+int(s2[-1].translate(ts)))%10!=int(s3[-1].translate(ts)):
        continue

    n1=int(s1.translate(ts))
    n2=int(s2.translate(ts))
    n3=int(s3.translate(ts))
    if n1+n2==n3 and len(str(n1))==len(s1) and len(str(n2))==len(s2) and len(str(n3))==len(s3):
        print(n1)
        print(n2)
        print(n3)
        exit()
print('UNSOLVABLE')