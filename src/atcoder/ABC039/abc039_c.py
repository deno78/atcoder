s=input()

ans=['Do','Do#','Re','Re#','Mi','Fa','Fa#','So','So#','La','La#','Si','Do']
key='WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'

for i in range(len(key)):
    key2=key[i:i+20]
    if s==key2:
        print(ans[i])
        exit()