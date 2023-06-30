x=input().split()
y=input().split()
print("YNEOS"[int(x[0] not in y and x[1] not in y)::2])