# TODO edit the code

# param
w = int(input())

# solve
ans = []
a1=w//3+1
a2=a1-1
ans.append(str(a1))
ans.append(str(a2))
for i in range(1,a2):
    ans.append(str(i))
if "0" in ans:
    ans.remove("0")
# answer
print(len(ans))
print(" ".join(ans))
