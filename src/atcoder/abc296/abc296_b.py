# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
slist=[]
for i in range(8):
    slist.append(input())

# solve
x=-1
y=-1
for i in range(8):
    for j in range(8):
        if slist[i][j]=="*":
            x=i
            y=j
            break
    if x!=-1 and y!=-1:
        break
#print("{}/{}".format(x,y))

# answer
x2=int(7-x+1)
y2=list("abcdefgh")[y]

print("{}{}".format(y2,x2))