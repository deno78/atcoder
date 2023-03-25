n = int(input(''))
alist = list(map(int,input('').split()))

#print(alist)
h=0
pre=0
for a in alist:
    if pre>0 and pre>a:
        h+=(pre-a)
#        print('{}->{}[{}]'.format(a,pre,h))
    if a > pre:
        pre=a

print(h)        
    
