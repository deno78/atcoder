x=input()
ans=0
# 文字列として桁ごとに分解して加算
for c in x:
    ans+=int(c)
print(ans)

