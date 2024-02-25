# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()
q = int(input())
cd = []
for i in range(q):
    c,d = input().split()
    cd.append([c,d])

# solve
src="abcdefghijklmnopqrstuvwxyz"
dst="abcdefghijklmnopqrstuvwxyz"
for c,d in cd:
    dst=dst.replace(c,d)

sdict={}
for i in range(len(src)):
    sdict[src[i]]=dst[i]

ans=[]
for i in range(len(s)):
    ans.append(sdict[s[i]])

# answer
print("".join(ans))

#laklimamriiamrmrllrmlrkramrjimrial
#lakmimamiiiamimillimmrkiamijimiial