n,q=map(int,input().split())

tiles=[False]*n
tile_colors=[""]*n
exception_colors=[""]*n
exception_epochs=[-1]*n
current_color="a"
current_epoch=0

for _ in range(q):
    query=input().split()
    if query[0]=="1":
        index=int(query[1])-1
        if tiles[index]:
            tiles[index]=False
            exception_colors[index]=tile_colors[index]
            exception_epochs[index]=current_epoch
        else:
            tiles[index]=True
            if exception_epochs[index]==current_epoch:
                tile_colors[index]=exception_colors[index]
            else:
                tile_colors[index]=current_color
    else:
        current_color=query[1]
        current_epoch+=1

answer=[]
for index in range(n):
    if tiles[index]:
        answer.append(tile_colors[index])
    elif exception_epochs[index]==current_epoch:
        answer.append(exception_colors[index])
    else:
        answer.append(current_color)

print("".join(answer))
