n=int(input())

i=0
x=1
while True:
    x*=2
    if x>n:
        print(i)
        exit()
    i+=1
