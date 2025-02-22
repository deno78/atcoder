# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = list(input())
if len(s)<2:
    print("".join(s))
    exit()

# solve
i=0
l=len(s)-1
while i<l:
#    print("[{}]:{} {}".format(i,s[i],s))
    if s[i]=="W" and s[i+1]=="A":
        s[i]="A"
        s[i+1]="C"
        i-=1
        i=max(i,0)
    else:
        i+=1

# answer
print("".join(s))