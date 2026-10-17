s1=input()
s2=input()

if s1[0]=="A" and s1[1]=="D" or \
    s2[0]=="A" and s2[1]=="D" or \
    s1[0]=="A" and s2[0]=="D" or \
    s1[1]=="A" and s2[1]=="D" or \
    s1[0]=="D" and s1[1]=="A" or \
    s2[0]=="D" and s2[1]=="A" or \
    s1[0]=="D" and s2[0]=="A" or \
    s1[1]=="D" and s2[1]=="A":
    print("Yes")
else:
    print("No")