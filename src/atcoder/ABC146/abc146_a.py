# 正攻法、曜日名の配列を作って検索
print(["SAT","FRI","THU","WED","TUE","MON","SUN"].index(input())+1)
# 少し横着、文字列にマッチする箇所を探して、単語帳＝３で割って位置を求める。
print("SATFRITHUWEDTUEMONSUN".find(input())//3+1)
