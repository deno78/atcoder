# TODO edit the code

# param
h1,h2,h3,w1,w2,w3=map(int,input().split())


# solve
ans = 0

# a1,a2,a3 = h1
# b1,b2,b3 = h2
# c1,c2,c3 = h3
# w1,w2,w3


for a1 in range(1,h1-1):
    for a2 in range(1,h1-a1):
        a3 = h1-a1-a2
        if a3 > 0:
            for b1 in range(1,h2-1):
                for b2 in range(1,h2-b1):
                    b3=h2-b1-b2
                    c1=w1-a1-b1
                    c2=w2-a2-b2
                    c3=w3-a3-b3
                    if c1 > 0 and c2 > 0 and c3>0 and b3 > 0 and (c1+c2+c3==h3):
                        ans+=1

# answer
print(ans)
