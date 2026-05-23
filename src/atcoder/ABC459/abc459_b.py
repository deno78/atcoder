n=int(input())
slist=input().split()

clist=[0]*n
for i in range(n):
    s=slist[i]
    if s[0] in "abc":
        clist[i]=2
    elif s[0] in "def":
        clist[i]=3
    elif s[0] in "ghi":
        clist[i]=4
    elif s[0] in "jkl":
        clist[i]=5
    elif s[0] in "mno":
        clist[i]=6
    elif s[0] in "pqrs":
        clist[i]=7
    elif s[0] in "tuv":
        clist[i]=8
    elif s[0] in "wxyz":
        clist[i]=9

clist2=[]
for i in range(n):
    clist2.append(str(clist[i]))

print("".join(clist2))