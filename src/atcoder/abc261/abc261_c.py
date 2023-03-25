# TODO edit the code

# param
n = int(input())
slist=[]
sdic2={}
for i in range(n):
    s=input()
    slist.append(s)
    if s not in sdic2.keys():
        sdic2[s]=0

# solve
for i in range(n):
    s=slist[i]
    c=sdic2[s]
    sdic2[s]+=1
    if c==0:
        print(s)
    else:
        print("{}({})".format(s,str(c)))

