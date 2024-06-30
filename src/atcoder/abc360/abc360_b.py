# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s,t = input().split()

# solve
for w in range(1,len(s)-1):
    for c in range(w+1):
        x=[]
        for i in range(len(s)//w+1):
            if c+(i*w)<len(s):
                x.append(s[c+(i*w)])
#        print("{} {} {}".format(w,c,x))
        if "".join(x)==t:
            print("Yes")
            exit()



# answer
print("No")
