# TODO edit the code

# param
a,n = map(int,input().split())

# solve

ans=0
que=[]
que.append(1)
cnt=0
while True:
    q=que.pop(0)
    q1=q*a
    if q1 not in que:
        que.append(q1)
        cnt+=1
    if q>9:
        q2=str(q)
        for _ in range(len(q2)-1):
            q2=q2[-1]+q2[:-1]
            if int(q2) not in que:
                que.append(int(q2))
                cnt+=1
    ans+=1
    print(que)
    if n in que:
        break

# answer
print(ans)
print(cnt)