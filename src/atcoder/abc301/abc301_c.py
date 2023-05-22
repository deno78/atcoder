# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
t = input()

# solve
sdict={}
tdict={}

for c in list("@abcdefghijklmnopqrstuvwxyz"):
    sdict[c]=0
    tdict[c]=0

for c in s:
    sdict[c]+=1
for c in t:
    tdict[c]+=1

cs=sdict["@"]
ct=tdict["@"]

# answer
for c in list("abcdefghijklmnopqrstuvwxyz"):
    if sdict[c]!=tdict[c]:
        if c in list("atcoder"):
            if sdict[c]>tdict[c]:
                ct-=(sdict[c]-tdict[c])
            else:
                cs-=(tdict[c]-sdict[c])
        else:
            print("No")
            exit()
if cs==ct and cs >= 0 and ct >= 0:
    print("Yes")
else:
    print("No")
