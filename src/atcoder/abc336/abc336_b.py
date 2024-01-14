# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
s=bin(n)[2:]

ans=0
for i in range(len(s)):
    p=-1 + (i*-1)
#    print("[{}] {}".format(p,s[p]))
    if s[p]=="0":
        ans+=1
    else:
        break

# answer
print("{}".format(ans))
