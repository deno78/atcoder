abcd  = input('').split()

a=int(abcd[0])
b=int(abcd[1])
c=int(abcd[2])
d=int(abcd[3])

ac=a*c
ad=a*d
bc=b*c
bd=b*d
print(max([ac,ad,bc,bd]))
