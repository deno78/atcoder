n,m=map(int,input().split())

ab=[]
for i in range(n):
    ab.append(set())
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab[a].add(b)
    ab[b].add(a)

result=[]

for i in range(n):
    # count trios that are non-hostile to user i
    hostile=ab[i]
    k=(n-1)-len(hostile)
    if k<3:
        result.append("0")
    else:
        result.append(str(k*(k-1)*(k-2)//6))

print(" ".join(result))