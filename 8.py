import itertools

n = 0
mn = []
for i in itertools.product("ольга", repeat=5):
    data = ''.join(i)
    n += 1
    mn.append(data)
mn = sorted(mn)
print(mn.index("ольга") + 1)