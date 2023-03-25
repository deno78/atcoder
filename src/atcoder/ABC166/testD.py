x = int(input(''))

can = []
for a in range(10**3):
    a5 = a**5
    if not a5 in can:
        can.append(a5)

result = []
for a in can:
    for b in can:
        if a - b == x:
            ans = "{} {}".format(int(a**(1/5)),int(b**(1/5)))
            if not ans in result:
                result.append(ans)
        if a + b == x and a > b:
            ans = "{} {}".format(int(a**(1/5)),int(-1 * b**(1/5)))
            if not ans in result:
                result.append(ans)

for r in result:
    print(r)