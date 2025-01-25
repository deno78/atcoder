# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a1,a2,a3,a4,a5=map(int, input().split())

# solve
ans=0
if (a1==2 and a2==1 and a3==3 and a4==4 and a5==5):
    print("Yes")
elif (a1==1 and a2==3 and a3==2 and a4==4 and a5==5):
    print("Yes")
elif (a1==1 and a2==2 and a3==4 and a4==3 and a5==5):
    print("Yes")
elif (a1==1 and a2==2 and a3==3 and a4==5 and a5==4):
    print("Yes")
else:
    print("No")
