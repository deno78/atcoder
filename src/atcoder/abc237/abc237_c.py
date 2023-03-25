import re

s = input()

cl=0
cr=0
for i in range(len(s)):
    if s[i]!='a':
        break
    cl+=1
for i in range(len(s)):
    if s[len(s)-i-1]!='a':
        break
    cr+=1

print(cl)
print(cr)
s2=s[cl:len(s)-cr-1]


# answer
if str(s2)==str(s2[::-1]):
    print('Yes')
else:
    print('No')
