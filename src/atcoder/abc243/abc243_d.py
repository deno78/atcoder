# TODO edit the code
 
# param
n,x = map(int,input().split())
s=input()

while ("RU" in s or "LU" in s):
    s=s.replace("RU","")
    s=s.replace("LU","")
# print(s)
# solve
for c in list(s):
    if c=="U":
        x=x//2
    elif c=="L":
        x=x*2
    elif c=="R":
        x=x*2+1
#    print("[{}] {} -> {}".format(c,x1,x))
 
# answer
print(x)
