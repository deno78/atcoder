# TODO edit the code

# param
s,t=input().split()
a,b=map(int,input().split())
u=input()

if u==s:
    a-=1
elif t==u:
    b-=1

# answer
print("{} {}".format(a,b))
