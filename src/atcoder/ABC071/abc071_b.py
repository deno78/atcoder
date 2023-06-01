a='abcdefghijklmnopqrstuvwxyz'
s=input()

for c in a:
    if c not in s:
        print(c)
        exit()
print("None")