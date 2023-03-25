s=list(input())

word=[]

for c in s:
    if c=='0' or c=='1':
        word.append(c)
    elif c=='B' and len(word)>0:
        del word[-1]
        
    
print("".join(word))