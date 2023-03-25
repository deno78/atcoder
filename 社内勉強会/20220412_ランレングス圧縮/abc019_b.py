from itertools import groupby

s=input()

g=groupby(list(s))

ans=[]
for k,v in g:
    ans.append("{}{}".format(k,len(list(v))))

print("".join(ans))