# TODO edit the code

# param
t = int(input())
q=[]
for i in range(t):
    q.append(list(map(int,input().split())))

for a,s in q:
    ans='No'
    for x in reversed(range(s//2+1)):
        y=s-x
        a2=(x&y)
        if a==a2:
            ans='Yes'
            break
    print(ans)
