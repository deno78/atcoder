# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s1,s2 = input().split()

# solve
if s1=="sick" and s2=="sick":
    print(1)
elif s1=="sick" and s2!="sick":
    print(2)
elif s1!="sick" and s2=="sick":
    print(3)
elif s1!="sick" and s2!="sick":
    print(4)