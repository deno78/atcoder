from collections import Counter

n=int(input())
alist=list(map(int,input().split()))
counter=Counter(alist)

max_len=max(counter)
diff=[0]*(max_len+2)
for length,count in counter.items():
    # Use a difference array so we can know how many repunits affect each digit.
    diff[0]+=count
    diff[length]-=count

digits=[]
carry=0
covering=0
for pos in range(max_len):
    covering+=diff[pos]
    value=covering+carry
    digits.append(value%10)
    carry=value//10

while carry:
    digits.append(carry%10)
    carry//=10

if not digits:
    digits.append(0)

while len(digits)>1 and digits[-1]==0:
    digits.pop()

print("".join(str(d) for d in reversed(digits)))