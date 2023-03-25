abc=list(map(int,input().split()))

# 愚直に場合分け
if abc[0]==abc[1]:
    print(abc[2])
elif abc[1]==abc[2]:
    print(abc[0])
elif abc[2]==abc[0]:
    print(abc[1])