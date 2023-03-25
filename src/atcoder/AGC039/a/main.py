s=list(input())
k=int(input())

cnt=0 # 変更が必要な回数

# 入力値の長さが1なら、繰り返し回数だけ変更が必要
if len(s)==1:
    print(k//2)
    exit()

# 全部同じ文字なら、文字の長さ*k/2だけ
if len(set(s))==1:
    print(len(s)*k//2)
    exit()

# sの中の繰り返し回数 x k
words=[1]
mod_margin=False
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        words[-1]+=1
        # 末尾の編集が必要な場合、先頭と末尾を変える必要は無くなる
        if i==0 or i==len(s)-2:
            mod_margin=True
    else:
        words.append(1)

cnt2=0
for w in words:
    if w>1:
        cnt2+=w//2
        #print("{} <-{}".format(w,w//2))
cnt+=cnt2*k
#print(words)

# 先頭と末尾が同じ場合、繰り返し毎に変更する必要がある。
if s[0] == s[-1] and not mod_margin:
    cnt+=(k-1)

print(cnt)