n=int(input())
s=input()

i1=s.index("|")
i3=s.index("|",i1+1)
i2=s.index("*")
if i1 < i2 and i2 < i3:
    print("in")
else:
    print("out")