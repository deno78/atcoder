alist = list(map(int,input().split()))

if len(set(alist))==2 and (alist.count(alist[0])==3 or alist.count(alist[0])==2):
    print("Yes")
else:
    print("No")