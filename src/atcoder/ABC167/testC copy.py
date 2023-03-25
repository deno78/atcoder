n=100
n2=2**n
print("loop:{}".format(n2))

for i in range(n2):
    buylist=[False]*n

    for j in range(n):
        print("\ti:{}[{}] j:{} =>{}".format(i,bin(i),j,i>>j&1))
        if int(i>>j&1) == 1:
            buylist[j]=True

    print("[{}] ->[{}]".format(i,buylist))
