lst = []
for i in range(1000):
    s = bin(i)[2:]
    s = str(s)
    if i % 3 == 0:
        s += s[-3:]
    else:
        s += bin(3 * (i % 3))[2:]
    r = int(s, 2)
    if r > 76:
        lst.append(i)
print(min(lst))
