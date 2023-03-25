# TODO edit the code

# param
n = int(input())
s,t=input().split()

s2=list(s)
t2=list(t)
# solve
ans = []
for i in range(n*2):
    if i%2==0:
        ans.append(s2[i//2])
    else:
        ans.append(t2[i//2])

# answer
print("".join(ans))
