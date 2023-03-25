x,y=map(int,input().split('.'))

if y>=0 and y<=2:
    print("{}-".format(x))
elif y>=3 and y<=6:
    print("{}".format(x))
elif y>=7 and y<=9:
    print("{}+".format(x))
