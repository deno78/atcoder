# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param


def resolve(sx,sy,tx,ty):
    # solve
    ans = abs(sy-ty)
    if sy%2==1:
        sx2=(sx-1)//2
    else:
        sx2=(sx)//2
    if ty%2==1:
        tx2=(tx-1)//2
    else:
        tx2=(tx)//2
    print("{} {}".format(sx2,tx2))
    d=abs(sx2-tx2)
    if sy%2!=ty%2:
        d+=1
    ans+=max(0,d-(abs(sy-ty)+1)//2)

    # answer
    print("{} {} {} {}=>{}".format(sx,sy,tx,ty,ans))
    return ans


# sx,sy = map(int, input().split())
# tx,ty = map(int, input().split())
# print(resolve(sx,sy,tx,ty))


assert(resolve(0,0,0,0)==0)
assert(resolve(0,0,0,1)==1)
assert(resolve(0,0,0,2)==2)
assert(resolve(0,0,0,3)==3)
assert(resolve(0,0,0,4)==4)
assert(resolve(0,0,1,0)==0)
assert(resolve(0,0,2,0)==1)
assert(resolve(0,0,3,0)==1)
assert(resolve(0,0,4,0)==2)

assert(resolve(1,1,1,1)==0)
assert(resolve(1,1,2,1)==0)
assert(resolve(1,1,3,1)==1)
assert(resolve(1,1,4,1)==1)

assert(resolve(1,1,1,2)==1)
assert(resolve(1,1,1,3)==2)
assert(resolve(1,1,1,4)==3)

assert(resolve(0,0,1,1)==1)
assert(resolve(0,0,2,1)==1)
assert(resolve(0,0,3,1)==2)
assert(resolve(0,0,4,1)==2)
