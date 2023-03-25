a=set(input().split())
if len(a)==1:print(list(a)[0])
else:print(list(set(['0','1','2']) - a)[0])