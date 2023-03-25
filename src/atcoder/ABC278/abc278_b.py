h,m=map(int,input().split())

while True:
    h1=str(h).zfill(2)[0]
    h2=str(h).zfill(2)[1]

    m1=str(m).zfill(2)[0]
    m2=str(m).zfill(2)[1]

    ha=int(h1+m1)
    ma=int(h2+m2)
#    print("{}{} {}{}".format(h1,h2,m1,m2))
    if ha < 24 and ma < 60:
        print("{} {}".format(h,m))
        exit()
    m+=1
    if m==60:
        h+=1
        h=h%24
        m=0
     
