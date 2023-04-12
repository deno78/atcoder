s=input()
t=input()

for i in range(len(s)):
    s2=s[i:] + s[:i]
    if s2==t:
        print("Yes")
        exit()

print("No")