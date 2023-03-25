s=input()
words=["eraser","erase","dreamer","dream"]

for w in words:
    while s.count(w)>0:
        s=s.replace(w,"")

if len(s)>0:
    print("NO")
else:
    print("YES")
