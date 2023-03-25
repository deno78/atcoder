import re
s = input()

pattern = re.compile('(dream|dreamer|erase|eraser)+')
res = pattern.fullmatch(s)
if res is not None:
    print('YES')
else:
    print('NO')