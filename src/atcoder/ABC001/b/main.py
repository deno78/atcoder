m=int(input())/1000
if m<0.1:
    print('00')
elif m>=0.1 and m<=5:
    print("{:02}".format(int(m*10)))
elif m>=6 and m<=30:
    print("{:02}".format(int(m+50)))
elif m>=35 and m<=70:
    print("{:02}".format(int((m-30)//5+80)))
elif m>70:
    print("89")