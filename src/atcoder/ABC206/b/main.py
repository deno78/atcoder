n=int(input())

m=0
d=0
while True:
    d+=1
    m+=d
    if m>=n:
        print(d)
        exit()