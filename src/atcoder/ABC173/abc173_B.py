n = int(input(''))
c0=0 # AC
c1=0 # WA
c2=0 # TLE
c3=0 # RE
for i in range(n):
    s = input('')
    if s == 'AC':
        c0+=1
    elif s=='WA':
        c1+=1
    elif s=='TLE':
        c2+=1
    elif s=='RE':
        c3+=1

print('AC x {}'.format(c0))
print('WA x {}'.format(c1))
print('TLE x {}'.format(c2))
print('RE x {}'.format(c3))
