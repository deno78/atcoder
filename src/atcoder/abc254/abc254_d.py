# TODO edit the code
def make_divisors(x,y):
    i = x
    x2=x**2
    ret=0
    ary=[]
    c=1
    while i>0 and x2//i<y:
        if x2 % i == 0:
            ary.append([i,x2//i])
            ret+=2
        i-=1
        c+=1
#    print("[{}]c:{} a:{} [{}]".format(x,c,len(ary),ary))
    return ret


# param
n = int(input())
#n=2*(10**4)

# solve
ans=0
for i in range(1,n+1):
    d=make_divisors(i,n)
    ans+=d

# answer
print(ans)
