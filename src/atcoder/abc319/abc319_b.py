# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i<=9:
                lower_divisors.append(i)
            if i != n // i:
                if n//i<=9:
                    upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# param
n = int(input())

dlist=make_divisors(n)
dlist.sort()
# solve
ans=[]
for i in range(n+1):
    ok=False
    for j in dlist:
        if i%(n//j)==0:
            ans.append(str(j))
            ok=True
            break
    if ok==False:
        ans.append("-")

# answer
print("".join(ans))