# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
dict=[]
for i in range(h):
    dict.append(list(map(int,input().split())))

# solve
wk=[]
wk.append([0,0,[dict[0][0]]])

ans=0
while len(wk)>0:
    z=wk.pop(0)
    x=z[0]
    y=z[1]
    if x==w-1 and y==h-1:
        ans+=1
    else:
        a=z[2]
        if y+1<h:
            a1=dict[y+1][x]
            if a1 not in a:
                an=a+[a1]
                wk.append([x,y+1,an])
        if x+1<w:
            a2=dict[y][x+1]
            if a2 not in a:
                an=a+[a2]
                wk.append([x+1,y,an])

# answer
print(ans)