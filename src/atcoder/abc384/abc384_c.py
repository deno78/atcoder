# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
score = list(map(int, input().split()))
user=["ABCDE",
"BCDE",
"ACDE",
"ABDE",
"ABCE",
"ABCD",
"CDE",
"BDE",
"ADE",
"BCE",
"ACE",
"BCD",
"ABE",
"ACD",
"ABD",
"ABC",
"DE",
"CE",
"BE",
"CD",
"AE",
"BD",
"AD",
"BC",
"AC",
"AB",
"E",
"D",
"C",
"B",
"A"]

# solve
d={}
score_list=[]
for i in range(len(user)):
    u=user[i]
    s=0
    for i in range(5):
        c=list("ABCDE")[i]
        if c in u:
            s+=score[i]
    if s not in d.keys():
        d[s]=[]
    d[s].append(u)
    score_list.append(s)

score_list=list(set(score_list))
score_list.sort(reverse=True)

for s in score_list:
    d[s].sort()
    for u in d[s]:
        print(u)

