# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
s=[]
for i in range(h):
    s.append(list(input()))

# solve
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            wk=[]
            wk.append([i,j])
            while len(wk)>0:
                item=wk.pop(0)
                y=item[0]
                x=item[1]
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        x2=min(max(x+dx,0),w-1)
                        y2=min(max(y+dy,0),h-1)
                        if s[y2][x2]=="#":
                            s[y2][x2]=str(ans)
#                            print("{} {}:{}".format(x2,y2,ans))
                            wk.append([y2,x2])
            ans+=1
#for l in s:
#    print("".join(l))

# answer
print("{}".format(ans))
