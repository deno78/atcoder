n=int(input())
s=input()

l=s.index("(")
ps=s
while True:
    for r in range(l+1,n):
        print("{}-{}={}".format(l,r,s[l:r]))
        if s[r]==")":
            s=s[:l] + s[r:]
            print(s)
            l=s.index("(")
            break
        if s[r]=="(":
            l=r
            break
    if s==ps:
        break
    ps=s
