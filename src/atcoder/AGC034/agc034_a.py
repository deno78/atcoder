n,a,b,c,d=map(int,input().split())
s=input()
a-=1
b-=1
c-=1
d-=1

if '##' in s[a:c] or '##' in s[b:d]:
    print('No')
    exit()

if (a-b)*(c-d)<0:
    if '...' not in s[b:d]:
        print('No')
        exit()

print('Yes')