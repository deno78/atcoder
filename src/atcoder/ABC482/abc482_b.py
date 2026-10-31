slist=[]
for _ in range(5):
    slist.append(input())

ans=5
for i in range(5):
    wk=slist[i].count("o")
#    print("#",slist[i],wk)
    ans=min(ans,5-wk)

dbg=[]
for i in range(5):
    wk=0
    dbg=[]
    for j in range(5):
        dbg.append(slist[j][i])
        if slist[j][i]=="o":
            wk+=1
    ans=min(ans,5-wk)
#    print("$","".join(dbg),wk)

dbg=[]
wk1=0
for i in range(5):
    dbg.append(slist[i][i])
    if slist[i][i]=="o":
        wk1+=1
#print("*","".join(dbg),wk1)
ans=min(ans,5-wk1)    
dbg=[]
wk2=0
for i in range(5):
    dbg.append(slist[i][i])
    if slist[4-i][4-i]=="o":
        wk2+=1
ans=min(ans,5-wk2)
#print("*","".join(dbg),wk2)

print(ans)
