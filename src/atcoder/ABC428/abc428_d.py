from bisect import bisect_left, bisect_right

t=int(input())
cases=[]
max_sq=0
for i in range(t):
    c,d=map(int,input().split())
    cases.append((c,d))
    cd=int(str(c)+str(c+d))
    max_sq=max(max_sq,cd)

squares=[]
squares2=[]
x=1
while x**2<=max_sq:
    squares.append(x**2)
    squares2.append(str(x**2))
    x+=1

for case in cases:
    c,d=case
    x=1
    ans=0
    a1=int(str(c)+str(c+1))
    a2=int(str(c)+str(c+d))
    str_c=str(c)
    idx1=bisect_left(squares,a1)
    idx2=bisect_right(squares,a2)

    for i in range(idx1, idx2):
        str_s=squares2[i]
        if str_s.startswith(str_c) and not str_s.startswith(str_c+"0"):
            ans+=1
#            print(c,d, s)
    print(ans)

 