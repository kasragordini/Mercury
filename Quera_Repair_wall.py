x, y = input().split()
x = int(x)
y = int(y)
r = int(input())
dx, dy = input().split()
dx = int(dx)
dy = int(dy)
if x <= dx <= x + r and y - r <= dy <= y :
    print("Mahdi")
else :
    print("Parsa")