# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
ans1=0
ans=[]
for i in range(n+1):
    ans.append([0]*(n+1))
for i in range(m):
    u,v = map(int, input().split())
    u-=1
    v-=1
    if u==v:
        ans1+=1
    elif ans[u][v]>0:
        ans1+=1
    else:
        ans[u][v]+=1
        ans[v][u]+=1

# solve
# wk=[]
# wk.append(0)
#ans2=0
# while len(wk)>0:
#     w=wk.pop(0)
#     if w in r.keys():
#         for y in r[w]:
#             ans[w][y]+=1
#             ans[y][w]+=1
#             if ans[w][y]==1:
#                 wk.append(y)
#             elif ans[w][y]==3:
#                     ans2+=1
# #                    print("{}->{}".format(w,y))
#         r[w]=[]

# answer
print(ans1)