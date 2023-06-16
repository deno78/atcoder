h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(input().split())

print("".join(["#"]*(w+2)))
for i in range(h):
    l=a[i]
    l.insert(0,"#")
    l.append("#")
    print("".join(l))
print("".join(["#"]*(w+2)))
