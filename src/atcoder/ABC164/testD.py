s = input('')
max_s = int(int(s)/2019)
rec = 0
for m in range(max_s+1):
    ms=str(2019*m)
    if not '0' in ms:
        idx=s.find(ms)
        while idx >= 0:
            rec+=1
            idx=s.find(ms,idx+1)
#            print("{} {}".format(ms,idx))
print(rec)
