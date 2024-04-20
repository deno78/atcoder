# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
for i in range(1,350):
    if s == "ABC" + str(i).zfill(3) and i != 316:
        print("Yes")
        exit()
print("No")

# answer
