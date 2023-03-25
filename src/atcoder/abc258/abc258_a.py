# TODO edit the code

# param
k = int(input())

h=k//60
m=k%60

# solve
ans = "{}:{}".format(21+h,str(0+m).zfill(2))

# answer
print(ans)
