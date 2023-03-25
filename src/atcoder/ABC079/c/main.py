a,b,c,d=map(int,list(input()))

op=["+","-"]

for o1 in op:
    for o2 in op:
        for o3 in op:
            ans=eval("{} {} {} {} {} {} {}".format(a,o1,b,o2,c,o3,d))
            if ans==7:
                print("{}{}{}{}{}{}{}=7".format(a,o1,b,o2,c,o3,d))
                exit()
