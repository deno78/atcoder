n=int(input())
alist=list(map(int,input().split()))
alist.sort()
all_sum = sum(alist)

ans = set()

def check(L):
    if L <= 0: return False
    if all_sum % L != 0:
        return False
    if alist[-1] > L:
        return False
    l_idx = 0
    r_idx = n - 1
    while l_idx <= r_idx:
        val_r = alist[r_idx]
        if val_r == L:
            r_idx -= 1
            continue
        if l_idx == r_idx:
            return False
        val_l = alist[l_idx]
        if val_l + val_r != L:
            return False
        l_idx += 1
        r_idx -= 1
    return True

cand1 = alist[-1]
if check(cand1):
    ans.add(cand1)

cand2 = alist[-1] + alist[0]
if check(cand2):
    ans.add(cand2)

sorted_ans = sorted(list(ans))
print(" ".join(map(str, sorted_ans)))