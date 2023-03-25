s = input('')
t = input('')

len_s=len(s)
len_t=len(t)

d=0
for j in range(len_t):
    if s[j]!=t[j]:
        d+=1
for i in range(len_s - len_t):
    s2 = s[i:i+len_t]
#    print(s2)
    d2=0
    for j in range(len_t):
        if s2[j]!=t[j]:
            d2+=1
#    print("{}/{}".format(s2,t))
    if d2<d:
        d=d2
print(d)

