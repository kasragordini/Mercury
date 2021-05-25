r, c = input().split()
c = int(c)
r = int(r)
if c <= 10 :
    a = int(11 - r)               #row from the entrance
    b = int(10 - abs(10 - c))     #absolute value #column from the entry
    print("right", a, b)
else :
    a = int(11 - r)               #row from the entrance
    b = int(11 - abs(10 - c))     #absolute value #column from the entry
    print("left", a, b)