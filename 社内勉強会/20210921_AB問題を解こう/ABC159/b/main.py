def check(b):
    for i in range(len(b)//2):
        i2=len(b)-i-1
        if b[i]!=b[i2]:
            return False
    return True

s=input()
n=len(s)
s1=s[0:(n-1)//2]
s2=s[(n+3)//2-1:]

if check(s) and check(s1) and check(s2):
    print('Yes')
else:
    print('No')