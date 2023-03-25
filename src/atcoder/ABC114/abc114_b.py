s = input('')

a=999
for i in range(len(s)-2):
    s2 = int(s[i:i+3])
    a = min(a,abs(s2-753))
#    print("[{}]{} {}".format(i,s2,a))

print(a)