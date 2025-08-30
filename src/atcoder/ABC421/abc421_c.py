n=int(input())
s=input()

idx=[]
for i in range(n*2):
    if s[i]=="A":
        idx.append(i)

wk1=0
for i in range(n):
    x=i*2
    y=idx[i]
    wk1+=abs(x-y)
wk2=0
for i in range(n):
    x=i*2+1
    y=idx[i]
    wk2+=abs(x-y)

print(min(wk1,wk2))