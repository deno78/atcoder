# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
D = input()

# solve
dlist=["N","NE","E","SE","S","SW","W","NW"]
idx=dlist.index(D)
idx=(idx+4)%len(dlist)

# answer
print("{}".format(dlist[idx]))
