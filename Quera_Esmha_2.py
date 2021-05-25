n = int(input())

s = []
for i in range(n):
    s.append(input())

print(max([len(set(i)) for i in s]))