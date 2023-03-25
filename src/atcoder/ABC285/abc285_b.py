n=int(input())
s=input()

for i in range(1,n):
    ans=0
    for j in range(i,n):
#        print("{}:{} / {}:{}".format(j,s[j],j-i,s[j-i]))
        if s[j] == s[j-i]:
            break
        ans+=1
    print(ans)


