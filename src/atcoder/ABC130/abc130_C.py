whxy = input('').split()
w = int(whxy[0])
h = int(whxy[1])
x = int(whxy[2])
y = int(whxy[3])

if x == w/2 and y == h /2:
    print(w*h/2,1)
else:
    print(w*h/2,0)