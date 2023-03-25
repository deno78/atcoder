# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
r,c = map(int, input().split())
dict=[]
for i in range(r):
    line=input()
    dict.append(list(line))

# solve
wall=[]
bomb=[]
for y in range(r):
    for x in range(c):
        if dict[y][x]=="#":
            wall.append([x,y])
        elif dict[y][x] != ".":
            bomb.append([x,y,int(dict[y][x])])

for b in bomb:
    x1=b[0]
    y1=b[1]
    d1=b[2]
    for w in wall:
        x2=w[0]
        y2=w[1]
        d2=abs(x1-x2)+abs(y1-y2)
        if d1>=d2:
            dict[y2][x2]="."
    dict[y1][x1]="."

# answer
for d in dict:
    print("".join(d))