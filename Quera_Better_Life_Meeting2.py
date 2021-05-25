r, c = input().split()
c = int(c)
r = int(r)
if c <= 10 :
    print("right", 10-r+1, c)
else :
    print("left", 10-r+1, 20-c+1)