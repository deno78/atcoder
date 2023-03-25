n=int(input())
s=input()
cdict={}
cdict["R"]=[]
cdict["G"]=[]
cdict["B"]=[]

for i in range(n):
    cdict[s[i]].append(i+1)

cdict["B"]=set(cdict["B"])
rcnt=len(cdict["R"])
gcnt=len(cdict["G"])
bcnt=len(cdict["B"])
ans=rcnt*gcnt*bcnt
#print(ans)
for i in range(len(cdict["R"])):
    r=cdict["R"][i]
    for j in range(len(cdict["G"])):
        g=cdict["G"][j]
        dset=set([])
        dset.add(2*r-g)
        dset.add(2*g-r)
        if abs(r+g)%2==0:
            dset.add(abs(r+g)//2)
#        print("R:{} G:{} diff:{}".format(r,g,dset & cdict["B"]))
        ans-=len(dset & cdict["B"])
print(ans)
