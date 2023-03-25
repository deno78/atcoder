s='ABC'
for i in range(5):
    buff=[]
    for c in list(s):
        if c=='A':
            buff.append("BC")
        elif c=='B':
            buff.append('CA')
        elif c=='C':
            buff.append('AB')
    s="".join(buff)
    print("[{}] {}".format(len(s),s))