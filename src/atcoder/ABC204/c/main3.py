import sys
sys.setrecursionlimit(10000)

# 深さ優先探索で全部調べていく
def fnc(pos):
    # 選択可能な枝を一つづつ
    for to in dlist[pos]:
        # 探索済みでなければ、掘っていく
        if to not in ans:
            ans.add(to)
            fnc(to)

nm=input().split()
n=int(nm[0])
m=int(nm[1])

# 経路データを連想配列で持つ。
# 　キー：遷移元
# 　値：遷移先のリスト
dlist={}
for i in range(n):
    dlist[i]=[]

# 入力値を受け取る
for i in range(m):
    ab=list(map(int,input().split()))
    a=ab[0]-1
    b=ab[1]-1
    dlist[a].append(b)

# 全部の開始点について、調べていく
cnt=0
for i in range(n):
    ans=set([i])
    fnc(i)
    cnt+=len(ans)
print(cnt)