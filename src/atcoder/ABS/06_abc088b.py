n = int(input(''))
alist = list(map(int,input().split(' ')))

a=0
b=0
turn = True
alist.sort(reverse=True)
for c in alist:
    if turn:
        a+=c
    else:
        b+=c
    turn = not turn

print(a-b)