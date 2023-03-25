# TODO edit the code

# param
a,b,c,x=map(int,input().split())

# solve
ans=0
if x<=a:
    ans=1
elif x >a and x<=b:
    ans=c/(b-a)


# answer
print(ans)
