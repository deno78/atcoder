n = int(input())
alist =sorted( list(map(int,input().split())))
alist.reverse()

list2=[]

c=0
a1 = 0
a2 = 0

for i in range(n):
    if i ==0:
        a1 = alist[i]
        c+=0
#        print("[{}]:{} gets 0".format(i,alist[i]))
    elif i==1:
        a2 = alist[i]
        c+=alist[0]
#        print("[{}]:{} gets {}".format(i,alist[i],a1))
    else:
        if a1 > a2:
            # a1の方が好感度高ければ、そちらにつけて、心地よさはa2を足す
            print("[{}]:{} gets {} ({}/{})".format(i,alist[i],a2,a1,a2))
            c+=a2
            a2 = alist[i]
        else:
            # a2の方が好感度高ければ、そちらにつけて、心地よさはa1を足す
            print("[{}]:{} gets {} ({}/{})".format(i,alist[i],a1,a1,a2))
            c+=a1
            a1 = alist[i]
print(c)