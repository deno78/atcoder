n=int(input())
s=input()

for i in range(n):
    c=s[i]
    if c=='1':
        if i%2==0:
            print('Takahashi')
        else:
            print('Aoki')
        exit()
