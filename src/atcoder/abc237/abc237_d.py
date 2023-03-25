# TODO edit the code
 
# param
n = int(input())
s=list(input())
 
a=['0']
# solve
l=0
for i in range(n):
    if s[i]== 'L':
        a.insert(l,str(i+1))
        l=l
    elif s[i]=='R':
        a.insert(l+1,str(i+1))
        l=l+1
ans=" ".join(a)
 
# answer
print(ans)