n=int(input())

cnt=0
for i in range(1,n+1):
    i2=oct(i)
    if '7' not in str(i) and '7' not in i2:
        cnt+=1
print(cnt)