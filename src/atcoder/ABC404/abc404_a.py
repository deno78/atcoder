s=input()
a="abcdefghijklmnopqrstuvwxyz"
for c in list(s):
    a=a.replace(c,"")

print(a[0])