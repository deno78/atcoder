x=input()

mod=True
while mod:
    mod=False
    for w in ["ch","o","k","u"]:
        if x.endswith(w):
            x=x[:-1*len(w)]
            mod=True

if len(x)==0:
    print("YES")
else:
    print("NO")
