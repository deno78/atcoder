s,a,b,x=map(int,input().split())

t1=x//(a+b)
t2=x-(t1*(a+b))

t2a=min(t2,a)*s

print(t1*s*a+t2a)