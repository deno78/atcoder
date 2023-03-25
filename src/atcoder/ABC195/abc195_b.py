import math
abw=input().split()
a=int(abw[0])
b=int(abw[1])
w=int(abw[2])*1000

x=math.floor(w/a) # 最小
y=math.ceil(w/b) # 最大

if x>0 and y>0 and x>=y:
    print('{} {}'.format(y,x))
else:
    print('UNSATISFIABLE')
