# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w = map(int, input().split())
slist=[]
for i in range(h):
    slist.append(list(input()))

# solve
word=list("snuke")
for i in range(h):
    for j in range(w):
        if slist[i][j]=="s":
            for dx in range(-1,2):
                for dy in range(-1,2):
                    s=[]
                    for d in range(5):
                        x2=i+dx*d
                        y2=j+dy*d
                        if x2 < h and y2 < w and x2 >=0 and y2 >=0:
                            s.append(slist[x2][y2])
                    if "".join(s)=="snuke":
                        for d in range(5):
                            x2=i+dx*d+1
                            y2=j+dy*d+1
                            print("{} {}".format(x2,y2))
