a=list(input())
b=list(input())
c=list(input())

t='a'
while True:
    if t=='a':
        if len(a)==0:
            print("A")
            exit()
        t2=a.pop(0)
    elif t=='b':
        if len(b)==0:
            print("B")
            exit()
        t2=b.pop(0)
    elif t=='c':
        if len(c)==0:
            print("C")
            exit()
        t2=c.pop(0)
    t=t2
