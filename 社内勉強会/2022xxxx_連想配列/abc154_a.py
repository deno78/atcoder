# TODO edit the code

# param
s,t=input().split()
a,b=map(int,input().split())
u=input()

# 数値を入れる連想配列を作る
d={}
d[s]=a
d[t]=b

# 入力文字をキーとして、該当する方を１減らす
d[u]-=1

# answer
print("{} {}".format(d[s],d[t]))
