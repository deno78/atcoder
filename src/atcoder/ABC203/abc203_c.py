nk=list(map(int,input().split()))
n=nk[0]
k=nk[1]

friends={}
for i in range(n):
    ab=list(map(int,input().split()))
    if ab[0] not in friends.keys():
        friends[ab[0]]=ab[1]
    else:
        friends[ab[0]]+=ab[1]

f = sorted(friends.items(), key=lambda x:x[0])
s=0
for a,b in f:
    if k<(a-s):
        print(s+k)
        exit()
    k-=(a-s)
    k+=b
    s=a

print(s+k)