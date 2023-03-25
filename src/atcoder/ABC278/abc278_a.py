n,k=map(int,input().split())
alist=input().split()

for i in range(k):
    alist.pop(0)
    alist.append("0")

print(" ".join(alist))
