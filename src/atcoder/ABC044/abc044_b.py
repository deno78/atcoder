w=input()

dic={}
for c in list(w):
    if c not in dic.keys():
        dic[c]=0
    dic[c]+=1

for v in dic.values():
    if v%2==1:
        print("No")
        exit()

print("Yes")
exit()
