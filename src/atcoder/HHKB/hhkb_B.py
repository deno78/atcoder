hw = input('').split()
h = int(hw[0])
w = int(hw[1])

slist = []
for i in range(h):
    s = input('')
    slist.append(s)

cnt=0
for i in range(h):
    for j in range(w):
        if i < h-1:
            if slist[i][j] == "." and slist[i+1][j] == ".":
                cnt+=1
        if j < w-1:
            if slist[i][j] == "." and slist[i][j+1] == ".":
                cnt+=1
print(cnt) 
            