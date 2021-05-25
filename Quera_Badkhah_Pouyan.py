p, d = [int(i) for i in input().split()]

n = 1
while True :
    if 0 <= (n*d) % p <= p/2 :
        print(n*d)
        break
    n += 1