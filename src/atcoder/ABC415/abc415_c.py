t=int(input())
ns=[]
for _ in range(t):
    n=int(input())
    s=input()
    ns.append([n,s])
print(ns)

for n,s in ns:
    wk=[]
    wk.append([0,0]) # pos,bitflag
    ok=False
    while len(wk)>0:
        w=wk.pop(0)
        pos=w[0]
        bit_flag=w[1]
        for i in range(n):
            idx=pos+i+1
            if idx<len(s) and s[idx]=="0":
                bit_flag2=bit_flag | (1<<i)  # iビット目を立てる
                print("# ",s ,bit_flag,bit_flag2,"/",(1<<n)-1,pos,i+1)
                if bit_flag2 == (1<<n)-1:  # 全てのビットが立っている場合
                    print("# ",s ,bit_flag,"/",(1<<n)-1,pos)
                    ok=True
                    break
                wk.append([idx,bit_flag2])
        if ok:
            print("Yes")
            break
    if not ok:
        print("No")