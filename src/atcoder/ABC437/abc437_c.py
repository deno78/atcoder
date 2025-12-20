T=int(input())
anslist=[]
for _ in range(T):
    n=int(input())
    wp=[]
    for i in range(n):
        wp.append(list(map(int,input().split())))
    
    # 貪欲法: W - P の小さい順（差の少ない順）に選ぶ
    total_p = sum(p for w, p in wp)
    items = sorted([w - p for w, p in wp])
    
    cumsum = 0
    ans = 0
    for i in range(n):
        cumsum += items[i]
        if cumsum >= 0:
            ans = i + 1
    
    anslist.append(ans)

for ans in anslist:
    print(ans)    
