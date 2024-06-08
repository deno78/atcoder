# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
MOD=998244353

# solve
ans=0
sz=n.bit_length()
for i in range(n):
    n=n<<(sz+1)
    print("[{}] {} {}".format(i,n,bin(n)))


# answer
print("{}".format(ans))
