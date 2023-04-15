# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
q = int(input())
box={}
card={}
for i in range(n+1):
    box[i]=[]
for i in range(q):
    p = input().split()
    i=int(p[1])
    if p[0]=="1":
        j=int(p[2])
        box[j].append(i)
        if i not in card.keys():
            card[i]=[]
        if j not in card[i]:
            card[i].append(j)
    elif p[0]=="2":
        box[i].sort()
        bs = [str(n) for n in box[i]]
        print(" ".join(bs))
    elif p[0]=="3":
        card[i].sort()
        cs = [str(n) for n in card[i]]
        print(" ".join(cs))

