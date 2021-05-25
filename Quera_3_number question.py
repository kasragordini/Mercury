a = float(input("number 1: "))
b = float(input("number 2: "))
c = float(input("number 3: "))
if a < b < c :
    print(c," is the greatest number and ") + (a, " is the smallest number") 
elif a < c > b :
    print(b," is the greatest number and ") + (a, " is the smallest number")
elif b < a < c :
    print(c," is the greatest number and ") + (b, " is the smallest number")
elif b < c < a :
    print(a," is the greatest number and ") + (b, " is the smallest number")
elif c < a < b :
    print(b," is the greatest number and ") + (c, " is the smallest number")
elif c < b < a :
    print(a," is the greatest number and ") + (c, " is the smallest number")