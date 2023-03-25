n=int(input()) # 最初の引数を受け取る
alist=[]       # 次からの入力を受け取るリスト
# 標準入力から順にN個受け取る
for i in range(n):
    alist.append(int(input()))
print(alist)