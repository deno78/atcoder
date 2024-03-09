# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
i1=s.index("|")
i2=s.index("|",i1+1)
# answer
print("{}{}".format(s[:i1],s[i2+1:]))
