n = int(input(''))
alist = list(map(int,input('').split(' ')))
 
alist.sort(reverse=True)
results = [True for i in range(n)]
 
for i in range(len(alist)):
    if results[i]!=False:
        ai = alist[i]
        result = False
        for j in reversed(range(i,len(alist))):
            result = True
            aj = alist[j]
#            print("{}[{}] {}[{}] {}/{}".format(ai,i,aj,j,(ai==aj),(ai%aj==0)))
            if i!=j and (ai==aj):
                results[j] = False
            if i!=j and (ai%aj  == 0):
                result = False
                break
        results[i] = result
 
print(results.count(True))