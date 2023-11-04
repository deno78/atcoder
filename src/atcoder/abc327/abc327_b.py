# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
b = int(input())

# solve
i=1
while True:
    if i**i==b:
        print(i)
        exit()
    elif i**i>b:
        break
    i+=1

print(-1)