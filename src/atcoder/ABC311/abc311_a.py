n=int(input())
s=input()
for i in range(len(s)+1):
    if "A" in s[:i] and "B" in s[:i] and "C" in s[:i]:
        print(i)
        exit()
