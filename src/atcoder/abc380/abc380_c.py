# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
s = input()

# solve
wk=0
in_1=False
l=-1
r=-1
ans=[]
for i in range(len(s)):
    c=s[i]
    if c=="1":
        if in_1 ==False:
            l=i
            in_1=True
    elif c=="0" and in_1==True:
        in_1=False
        r=i-1
        ans.append([l,r])
    if len(ans)==k:
        break

if in_1==True:
    ans.append([l,len(s)])

x=ans[-2]
y=ans[-1]

s1=s[:x[1]+1]
s2=s[y[0]:y[1]+1]
s3=s[x[1]+1:y[0]]
s4=s[y[1]+1:]

#print("{}-{}-{}-{}".format(s1,s2,s3,s4))
print(s1+s2+s3+s4)
