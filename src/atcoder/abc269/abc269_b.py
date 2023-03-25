s=[]
for i in range(10):
    s.append(list(input()))

a=-1
b=10
c=-1
d=10
for i in range(10):
    for j in range(10):
        if s[i][j]=="#":
            a=i
            c=j
            for k in range(i,10):
                if s[k][j]==".":
                    b=k
                    break
            for k in range(j,10):
                if s[i][k]==".":
                    d=k
                    break
            print("{} {}".format(a+1,b))
            print("{} {}".format(c+1,d))
            exit(0)

