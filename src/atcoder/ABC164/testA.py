sw = input('')
s = int(sw.split(' ')[0])
w = int(sw.split(' ')[1])
if s > w:
    print('safe')
else:
    print('unsafe')
