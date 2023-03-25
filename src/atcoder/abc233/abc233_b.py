# TODO edit the code

# param
l,r=map(int,input().split())
s=input()

# answer
print(
    s[0:l-1] +
    "".join(reversed(list(s[l-1:r])))
    + s[r:]
    )
