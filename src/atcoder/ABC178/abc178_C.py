n = int(input(''))

mod = 1000000007

cnt_all= 10**n%mod
cnt_90=8**n%mod
cnt_9=9**n%mod
cnt_0=cnt_9%mod
cnt=(cnt_all + cnt_90 - cnt_9 - cnt_0)%mod
#print("{} - {} - {} + {} = {}".format(cnt_all,cnt_9,cnt_0,cnt_90,cnt))
print(cnt)
