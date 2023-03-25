n = int(input(''))
s = input('')

c = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (s[i] != s[j] and s[i] != s[k] and s[j] != s[k]) and (j-i!=k-j):
#                print("{}:{}:{}".format(i,j,k))
                c+=1
print(c)

