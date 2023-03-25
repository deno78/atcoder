# TODO edit the code

# param
n = int(input())

# solve
ans = []
ans.append(["1"])

for i in range(1,n):
    ans.append([])
    ans[i].extend(ans[i-1])
    ans[i].append(str(i+1))
    ans[i].extend(ans[i-1])

#print(ans)
# answer
print(" ".join(ans[n-1]))
