# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans=0
for i in range(len(s)-1):
    a=s[i]
    if a=="A":
        for j in range(i+1,len(s)):
            b=s[j]
            if b=="B":
                x=j-i
                if j+x<len(s) and s[j+x]=="C":
                    ans+=1

# answer
print("{}".format(ans))
