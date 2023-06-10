# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
p,q = input().split()

d={}
d["A"]=0
d["B"]=3
d["C"]=4
d["D"]=8
d["E"]=9
d["F"]=14
d["G"]=23

# solve
ans = abs(d[p] - d[q])

# answer
print("{}".format(ans))
