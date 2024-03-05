import itertools
#
# n = 0
# mn = []
# for i in itertools.product("ольга", repeat=5):
#     data = ''.join(i)
#     n += 1
#     mn.append(data)
# mn = sorted(mn)
# print(mn.index("ольга") + 1)


n = 1
ans = 0
mn = []
for i in itertools.product("реплика",repeat=6):
    data = ''.join(i)
    if n % 2 == 0 and data[0] != "к" and data.count("и") > 1:
        ans += 1
    n += 1
print(ans)


