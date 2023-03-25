t = input('')

def check_score(s):    
    s1 = s.count('PD')
    s2 = s.count('D')
    return s1+s2

# ?の位置を調査
tlist = list(t)
qlist = []
for i in range(len(tlist)):
    if tlist[i] == '?':
        qlist.append(i)

n=len(qlist)
max_s = ''
max_c = 0
for i in range(2**n):
    tlist = list(t)
    s=''
    for j in range(n):
        idx = qlist[j]
        if ((i>>j) &1):
            tlist[idx] = 'P'
        else:
            tlist[idx] = 'D'
    st = "".join(tlist)
    score = check_score(st)
#    print("{}:{}".format(st,score))
    if score > max_c:
        max_c = score
        max_s = st

print("{}".format(max_s))