n=int(input())
s=input()
t=input()

for i in range(n):
    if t[i]!="*":
        if s[i]!=t[i]:
            print("No")
            exit()
print("Yes")