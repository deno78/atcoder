

def func(x):
    c1=x//11 * 2
    if x%11==0:
        c2=0
    elif x%11>=1 and x%11<=6:
        c2=1
    else:
        c2=2
    return c1+c2

x=int(input())
print(func(x))