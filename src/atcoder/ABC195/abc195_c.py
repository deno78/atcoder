n = input()

l=len(n)
cnt=0
ly=999
for i in range(4,l+1):
    x=(i-1)//3
    if i!=l:
        y=int("".join("9"*i))
#            print("[{}/{}] {}".format(i,x,y))
        cnt+= x*(y-ly)
        ly=y
    else:
        y=int("".join("9"*(i-1)))+1
        a=int(n[0])
        b=int(n[1:])
#        print("[{}/{}]# {} + {}".format(i,x,y*(a-1),b))
        cnt+=(x*y*(a-1) + b*x + x)

print(cnt)

#107730272137364
#107730272138364
