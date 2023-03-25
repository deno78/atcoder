print(input().replace("1","a").replace("9","1").replace("a","9"))
print(input().translate(str.maketrans({"1":"9","9":"1"})))
