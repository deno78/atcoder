# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def base_n(num_10,n):
    ret=[]
    while num_10:
        if num_10%n>=10:
            return -1
        ret.append(num_10%n)
        num_10 //= n
    ret.reverse()
#    print(ret)
    return ret

# param
n = int(input())
s=["0","2","4","6","8"]

if n==1:
    print(0)
    exit()

# solve
ans=[]
for i in base_n(n-1,5):
    ans.append(s[i])

# answer
print("".join(ans))