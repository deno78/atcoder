# TODO edit the code

# param
s=list(input())

# solve
for i in range(0,10):
    if str(i) not in s:
        print(str(i))
        exit()
