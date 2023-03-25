def count_ones_by_bitmask(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

abk=list(map(int,input().split()))
a=abk[0]
b=abk[1]
k=abk[2]
s=a+b

cnt=0
for i in range(k,2**(s)):
    if count_ones_by_bitmask(i)==b:
        cnt+=1
        if cnt==k-1:
            bit=[0]*(s)
            bc=0
            for j in range(s):
                if (i>>j)&1:
                    bit[j]=1
            result=[]
            for b in bit:
                if b==1:
                    result.append('b')
                else:
                    result.append('a')
            print("".join(reversed(result)))
            exit()
