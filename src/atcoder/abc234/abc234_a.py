def f(x):
    return x**2 + x*2+3

# TODO edit the code

# param
t = int(input())

# solve
ans = f(f(f(t)+t) + f(f(t)))

# answer
print(ans)
