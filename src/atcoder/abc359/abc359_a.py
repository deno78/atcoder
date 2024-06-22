# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

slist=[]
for i in range(n):
    s = input()
    slist.append(s)

# solve
ans=0
for i in range(n):
    if slist[i]=="Takahashi":
        ans+=1

# answer
print("{}".format(ans))
