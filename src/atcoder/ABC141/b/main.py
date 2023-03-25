s=input()

ok1=True
ok2=True
ptn1=list('RUD')
ptn2=list('LUD')
for i in range(len(s)):
    c=s[i]
#    print("[{}] {} ({},{})".format(i,c,c not in ptn1,c not in ptn2))
    # 奇数パターン
    if i%2==0 and c not in ptn1:
        ok1=False
    # 偶数パターン
    if i%2==1 and c not in ptn2:
        ok2=False
#print("{} or {}".format(ok1,ok2))
if ok1 and ok2:
    print('Yes')
else:
    print('No')
