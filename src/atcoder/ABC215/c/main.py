import itertools

sk=input().split()
s=sk[0]
k=int(sk[1])-1

words=[]
l=list(s)
for pair in itertools.permutations(l,len(l)):
    words.append("".join(pair))
words=list(set(words))
words.sort()
print(words[k])