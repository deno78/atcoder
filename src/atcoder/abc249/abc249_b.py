# TODO edit the code

# param
s=input()

a1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a2='abcdefghijklmnopqrstuvwxyz'


ok1=False
ok2=False
ok3=False

for c in list(s):
    if c in a1:
        ok1=True
    if c in a2:
        ok2=True

if len(list(set(list(s))))==len(list(s)):
    ok3=True


if ok1 and ok2 and ok3:
    print('Yes')
else:
    print('No')