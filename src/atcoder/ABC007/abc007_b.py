a=input()
if len(a)==1:
    if a=='a':
        print(-1)
    else:
        print(chr(ord(a)-1))
else:
    print(a[:-1])