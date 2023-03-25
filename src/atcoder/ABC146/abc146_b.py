n=int(input())
s=input()

a=[]
for c in s:
    # 文字コードを求めて、大文字Aのコードを引く＝アルファベット順を求める
    o=ord(c)-65 
    # N文字、位置をずらして、26で割って＝Z→Aループさせる
    o2=(o+n)%26 
    a.append(chr(o2 + 65)) # 文字に戻して追加。

# 文字列を結合させて表示
print("".join(a))
