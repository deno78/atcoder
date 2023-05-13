import re
a,b=input().split()
pattern="[0-9]{" + a + "}-[0-9]{" + b + "}"
if re.match(pattern,input()):
    print("Yes")
else:
    print("No")