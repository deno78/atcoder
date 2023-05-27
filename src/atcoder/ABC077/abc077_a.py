c1=input()
c2=input()
if c1 == "".join(reversed(c2)) and c2 == "".join(reversed(c1)):
    print("YES")
else:
    print("NO")