s=input()

k="keyence"

for i in range(len(s)):
    for j in range(i,len(s)):
        if  s[:i] + s[j:] == k:
            print("YES")
            exit()

print("NO")
