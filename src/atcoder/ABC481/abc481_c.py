q=int(input())

queries=[]
for i in range(q):
    queries.append(input())

id=0
names={}
for name in queries:
    if name in names.keys():
        print(names[name])
    else:
        id+=1
        names[name]=str(id)
        print(str(id))
