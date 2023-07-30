s=input()
ans=[]
for c in list('ABCDEF'):
    ans.append(str(s.count(c)))

print(" ".join(ans))