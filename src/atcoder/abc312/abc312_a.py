# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
for w in ["ACE","BDF","CEG","DFA","EGB","FAC","GBD"]:
    if s == w:
        print("Yes")
        exit()

# answer
print("No")