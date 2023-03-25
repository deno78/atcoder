def base(n, b):
    s = []
    p = abs(n)
    while p:
        s.append(p % b)
        p //= b
    alp = "abcdefghijklmnopqrstuvwxyz"
    r=''
    first = True
    for a in s:
        if first:
            r+=alp[a]
        else:
            r += alp[a-1]
        first = False
    ret  =''.join(list(reversed(r)))
    if ret.startswith('az'):
        ret.replace('az','z')
    return ret


n = int(input(''))-1
print("{}".format(base(n,26)))
