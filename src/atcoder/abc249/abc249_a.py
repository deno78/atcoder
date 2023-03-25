# TODO edit the code

# param
a,b,c,d,e,f,x=map(int,input().split())

ans1=x//(a+c)*a*b+min(a,x%(a+c))*b
ans2=x//(d+f)*d*e+min(d,x%(d+f))*e

if ans1==ans2:
    print("Draw")
elif ans1>ans2:
    print("Takahashi")
else:
    print("Aoki")