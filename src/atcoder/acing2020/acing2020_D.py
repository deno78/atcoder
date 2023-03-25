pcmap={}
answermap={}

def popcount(a):
    if a in pcmap.keys():
        return pcmap[a]
    else:
        s = str(bin(a))
        pcmap[a] = s.count('1')
        return pcmap[a]

def func(a):
    cnt=0
    while True:
        a2=popcount(a)
        if a2==0:
            break
        a %= a2
        cnt+=1
    return cnt

n = int(input(''))
x = input('')

for i in range(n):
    x2 = list(x)
    if x[i] =='0':
        x2[i] = '1'
    else:
        x2[i] = '0'
    x3 = int("".join(x2),2)
    if x3 in answermap.keys():
        print(answermap[x3])
    else:
        ans = func(x3)
        answermap[x3] = ans
        print(ans)
