s=list(input())

ok=True
for i in range(len(s)):
    if i%2==0 and s[i].isupper():
        ok=False
    if i%2==1 and s[i].islower():
        ok=False
print('Yes' if ok else 'No')